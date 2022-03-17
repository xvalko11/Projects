#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <string.h>
#include <fstream>
#include <netinet/ip_icmp.h>
#include <poll.h>
#include <openssl/aes.h>
#include <sys/stat.h>
#include <unistd.h>
#include "server.cpp"
using namespace std;

struct arguments
{
    string fileName;
    string ipHostname;
    bool serverArg = false;
    bool badArgsFlag = false;
};

struct fileInfo
{
    string name;
    long long size;
};

/*  The funtion gets size and name of file from path and returns it    */
fileInfo getFileInfo(string filePath)
{
    struct fileInfo toReturn;
    ifstream file(filePath, std::ios::in | std::ios::binary);
    unsigned found = filePath.find_last_of("/\\");
    toReturn.name = filePath.substr(found + 1);
    cout << toReturn.name << endl;
    if (file.is_open())
    {
        toReturn.size = file.gcount();
    }
    else
    {
        toReturn.size = -1;
    }

    return toReturn;
}

/*  The funtion first sends starting packet with filename which starts file transport and then sends all the other packets encrypted
    including the last one which ends the file transport    */
int send_file(int sock, string fileName, struct addrinfo *serverinfo)
{
    AES_KEY key_e;
    AES_set_encrypt_key((const unsigned char *)"xvalko11xvalko11", 128, &key_e); //sets encryption key for AES_encrypt
    struct fileInfo fileInfo = getFileInfo(fileName);
    if (fileInfo.size == -1)
    {
        fprintf(stderr, "UNABLE TO OPEN FILE \n");
        return 1;
    }

    ifstream file("./" + fileInfo.name, std::ios::in | std::ios::binary);
    if (file.is_open())
    {
        char packet[1500];
        memset(&packet, 0, 1500);
        string filenameLen;
        if (fileInfo.name.length() < 10)
        {
            filenameLen = "00" + to_string(fileInfo.name.length());
        }
        else if (fileInfo.name.length() < 100)
        {
            filenameLen = "0" + to_string(fileInfo.name.length());
        }
        else
        {
            filenameLen = to_string(fileInfo.name.length());
        }

        //first send START packet with length of filename and filename
        string data = "START:" + filenameLen + fileInfo.name;
        struct icmphdr *icmp_header = (struct icmphdr *)packet;
        icmp_header->code = ICMP_ECHO;
        icmp_header->checksum = 0;
        memcpy(packet + sizeof(struct icmphdr), &data[0], data.size());

        if (sendto(sock, packet, sizeof(struct icmphdr) + data.size(), 0, (struct sockaddr *)(serverinfo->ai_addr), serverinfo->ai_addrlen) < 0)
        {
            fprintf(stderr, "SENDTO ERROR\n");
            return 1;
        }
        unsigned char *memblock = new unsigned char[PACKETLEN];                                      //one block of memorry which is being sent
        unsigned char *output = (unsigned char *)calloc(AES_BLOCK_SIZE, PACKETLEN / AES_BLOCK_SIZE); //allocate for AES_encrypt function

        //struct required for polling
        struct pollfd fds[1];
        fds[0].fd = sock;
        fds[0].events = POLLOUT | POLLRDHUP | POLLERR | POLLNVAL;
        fds[0].revents = 0;

        //encrypt and send all the packets
        while (file.read((char *)memblock, PACKETLEN))
        {
            for (int i = 0; i < PACKETLEN; i += 16)
            {
                AES_encrypt(memblock + i, output + i, &key_e);
            }
            memcpy(packet + sizeof(struct icmphdr), output, PACKETLEN);
            if (int result = poll(fds, 1, 2000)) //wait until it is possible to use socket
            {
                if (result < 1)
                {
                    fprintf(stderr, "POLLING ERROR \n");
                    return 1;
                }
                else
                {
                    // see if event occurred - it is possible to use socket
                    if (fds[0].revents & POLLOUT)
                    {
                        usleep(200);
                        if (sendto(sock, packet, sizeof(struct icmphdr) + PACKETLEN, 0, (struct sockaddr *)(serverinfo->ai_addr), serverinfo->ai_addrlen) < 0)
                        {
                            fprintf(stderr, "SENDTO ERROR \n");
                            return 1;
                        }
                    }
                }
            }
        }
        //create last packet, variable mod is required for cyphre padding
        if (file.gcount() > 0)
        {
            int mod = file.gcount() % AES_BLOCK_SIZE;
            mod = AES_BLOCK_SIZE - mod;
            int x = file.gcount();
            string len;
            if (x < 1000)
            {
                len = "0" + to_string(x);
            }
            else
            {
                len = to_string(x);
            }
            for (int i = 0; i < x + mod; i += AES_BLOCK_SIZE) // simple encryption
                AES_encrypt(memblock + i, output + i, &key_e);
            string data = "END:" + len;
            memcpy(packet + sizeof(struct icmphdr), &data[0], data.size());                     //copy END:XXXX where XXXX is length of last packet
            memcpy(packet + sizeof(struct icmphdr) + data.size(), output, file.gcount() + mod); // copy other data
            if (sendto(sock, packet, sizeof(struct icmphdr) + file.gcount() + mod + data.size(), 0, (struct sockaddr *)(serverinfo->ai_addr), serverinfo->ai_addrlen) < 0)
            {
                fprintf(stderr, "SENDTO ERROR\n");
                return 1;
            }
        }
    }
    return 0;
}

/* The function gets info about server, creates socket and pass it to function send_file()  */
int client(string ipHostname, string fileName)
{
    int protocol;
    struct addrinfo hints, *serverinfo;
    memset(&hints, 0, sizeof(hints)); //set hints to zero
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_RAW;

    char *host = (char *)ipHostname.c_str();
    int result;

    if ((result = getaddrinfo(host, NULL, &hints, &serverinfo)) != 0)
    {
        fprintf(stderr, "ERROR : %s\n", gai_strerror(result));
        return 1;
    }

    if (serverinfo->ai_family == AF_INET)
    {
        protocol = IPPROTO_ICMP;
    }
    else if (serverinfo->ai_family == AF_INET6)
    {
        protocol = IPPROTO_ICMPV6;
    }

    int sock = socket(serverinfo->ai_family, serverinfo->ai_socktype, protocol);
    if (sock == -1)
    {
        fprintf(stderr, "UNABLE TO CREATE SOCKET\n");
        return 1;
    }
    send_file(sock, fileName, serverinfo);
    return 0;
}

/*  The function parses arguments and return them in structure  */
arguments parse_arguments(vector<string> args, int argc)
{
    arguments argsToReturn;
    bool sFlag = false;
    bool rFlag = false;
    if (argc == 2)
    {
        string x = args.front();
        if (x == "-l")
        {
            argsToReturn.serverArg = true;
            return argsToReturn;
        }
        else if (x == "-h" || x == "--help")
        {
            cout << "USE AS CLIENT : ./secret -s <ip|hostname> -r <filename> " << endl;
            cout << "USE AS SERVER : ./secret -l " << endl;
            exit(0);
        }
        else
        {
            argsToReturn.badArgsFlag = true;
            return argsToReturn;
        }
    }
    else if (argc == 5)
    {
        for (auto i = args.begin(); i != args.end(); ++i)
        {
            if ((*i == "-r") && !(rFlag))
            {
                argsToReturn.fileName = *++i;
                rFlag = true;
            }
            else if ((*i == "-s") && !(sFlag))
            {
                argsToReturn.ipHostname = *++i;
                sFlag = true;
            }
            else
            {
                argsToReturn.badArgsFlag = true;
                return argsToReturn;
            }
        }
    }
    else
    {
        argsToReturn.badArgsFlag = true;
        return argsToReturn;
    }
    return argsToReturn;
}

int main(int argc, char **argv)
{
    vector<string> args(argv + 1, argv + argc);
    arguments parsedArgs = parse_arguments(args, argc);
    int returncode;
    if (parsedArgs.badArgsFlag)
    {
        cout << "Bad parameters, for help use -h or -help" << endl;
        return 1;
    }
    else if (parsedArgs.serverArg)
    {
        returncode = server();
    }
    else
    {
        returncode = client(parsedArgs.ipHostname, parsedArgs.fileName);
    }
    return returncode;
}