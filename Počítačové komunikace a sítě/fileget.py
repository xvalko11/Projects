#!/usr/bin/env python3
import socket
import sys
import os
import argparse
from urllib.parse import urlparse

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str, help="SURL of file to download. Protocol is always fsp", dest="SURL")
    parser.add_argument("-n", type=str, help="IP adress and port of nameserver", dest="NAMESERVER")
    args=parser.parse_args()
    if args.SURL==None:
        sys.exit("Argument -f SURL is missing")
    if args.NAMESERVER==None:
        sys.exit("Argument -n NAMESERVER is missing")       
    surl=urlparse(args.SURL)
    nameserver=args.NAMESERVER.split(":")
    if len(nameserver) < 2: #bad nameserver adress
        sys.exit("ERR Syntax")
    return(surl,nameserver)

def getTcpAdress(domain,ip,port):
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    client.settimeout(30.0)
    UDP_MESSAGE="WHEREIS %s" % (domain)
    client.sendto(UDP_MESSAGE.encode('utf-8'), (ip,port))
    try:
        received_data = client.recvfrom(8192)
    except socket.timeout:
        sys.exit("ERROR TIMEOUT")
    if received_data[0].decode('utf-8') == "ERR Not Found":
        sys.exit("FILESERVER not found")
    else:
        fileserverName = received_data[0].decode('utf-8')[3:]
        tcpAdress=fileserverName.split(':')
    client.close()
    return tcpAdress[0],int(tcpAdress[1])

def downloadFile(filePath,fileName,domain,tcpAdress,downloadAll):
    file=os.path.join(filePath,fileName)
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.settimeout(30.0)
    TCP_MESSAGE="GET %s FSP/1.0\r\nHostname: %s\r\nAgent: xvalko11\r\n\r\n" %(file, domain)
    try:
        client.connect(tcpAdress)
    except socket.timeout:
        sys.exit("ERROR TIMEOUT")
    client.send(TCP_MESSAGE.encode('utf-8'))
    response=client.recv(8192).decode('utf-8')
    if response[:15]=="FSP/1.0 Success": 
        dataFinal = bytes()
        while True:
            dataBuffer = client.recv(8192)
            if not dataBuffer:
                break
            dataFinal += dataBuffer
        if downloadAll==False:
            f = open(fileName, "wb")
            f.write(dataFinal)
            f.close()
        elif downloadAll==True:
            if not os.path.exists('./'+filePath):
                os.makedirs(filePath)
            f = open(file, "wb")
            f.write(dataFinal)
            f.close()
    else:
        sys.exit("ERROR Not Found")

#####       MAIN         ######
(surl,nameserver)=parseArgs()

(filePath, fileName) = os.path.split(surl.path)
filePath=filePath[1:]
udp_ip=nameserver[0]
udp_port=int(nameserver[1])
udp_adress=(udp_ip,udp_port)
(tcp_ip, tcp_port)=getTcpAdress(surl.netloc,udp_ip,udp_port)

if fileName != "*":
    downloadFile(filePath, fileName, surl.netloc,(tcp_ip,tcp_port),False)
else:
    TCP_MESSAGE="GET index FSP/1.0\r\nHostname: %s\r\nAgent: xvalko11\r\n\r\n" %(surl.netloc)
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.settimeout(30.0)
    try:
        client.connect((tcp_ip,tcp_port))
    except socket.timeout:
        sys.exit("ERROR TIMEOUT")
    client.send(TCP_MESSAGE.encode('utf-8'))
    response=client.recv(8192).decode('utf-8')
    if response[:15]=="FSP/1.0 Success": 
        dataFinal = bytes()
        dataFinal = client.recv(8192)
        if(str(dataFinal)=="b''"):                          ## weird bug when sometimes index comes with header and sometimes not
            index=response.split('\r\n\r\n')
            index=index[1].split('\r\n')
            index.pop()
        else:
            index = dataFinal.decode('utf-8')
            index= index.split('\r\n')
            index.pop()
    else:
        sys.exit("ERROR WHEN DOWNLOADING INDEX")
    client.shutdown(socket.SHUT_RDWR)
    client.close()
    for i in index:
        (filePath, fileName) = os.path.split(i)
        downloadFile(filePath, fileName, surl.netloc,(tcp_ip,tcp_port),True)