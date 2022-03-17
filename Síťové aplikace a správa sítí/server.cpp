/* Časť kódu bola prevzatá z WISu / Soubory k předmětům / Síťové aplikace a správa sítí / Příklady / examples.zip / pcap / sniff-filter.c*/

#include <string.h>
#include <stdio.h>
#include <pcap.h>
#include <pcap/pcap.h>
#include <err.h>
#include <netinet/ip_icmp.h>
#include <fstream>
#include <netinet/ether.h>
#include <time.h>
#include <openssl/aes.h>

#define SIZE_ETHERNET_LINUX_CAPTURE (AES_BLOCK_SIZE)

const int PACKETLEN = 1376; // describes max number of bytes which is being sent in one packet
std::ofstream outfile;

int IPSIZE; //global var that is used to determine whether it is IPV4 or IPV6 header

/*  The function handles packets decrypts them and write to file, if there is START packet the function starts file transport 
    - if there is END packet the function stops file transport   */
void receive_file(const u_char *packet)
{
    AES_KEY key_d;
    AES_set_decrypt_key((const unsigned char *)"xvalko11xvalko11", 128, &key_d); //decryption key must be the same as encryption key
    unsigned char *data = new unsigned char[PACKETLEN];                         // one block of memmory
    data = (unsigned char *)packet + SIZE_ETHERNET_LINUX_CAPTURE + IPSIZE + sizeof(struct icmphdr);
    if (strncmp((char *)data, "START:", 6) == 0) //first packet looks like START:XXX------ where XXX is len of filename and --- is filename
    {
        data += 6;
        char tmp[3];
        char *endPtr;
        strncpy((char *)tmp, (char *)data, 3); //first get length of filename
        tmp[3] = '\0';                         //fixes bug with strncpy
        int length = strtol(tmp, &endPtr, 10);
        data += 3;
        char name[length];
        strncpy((char *)name, (char *)data, length);
        name[length] = '\0';                                 //fixes bug with strncpy
        outfile.open(name, std::ios::out | std::ios::trunc); //if there was already a file with the same name delete its content
        outfile.close();
        outfile.open(name, std::ios::app); // append instead of overwrite
    }
    else if (strncmp((char *)data, "END:", 4) == 0) //last packet looks like END:XXXX------ where XXXX is size of last packet and --- are last packet data
    {
        data += 4;
        char tmp[4];
        char *endPtr;
        strncpy((char *)tmp, (char *)data, 4); //get length of last packet
        tmp[4] = '\0';
        int length = strtol(tmp, &endPtr, 10);
        data += 4;
        int mod = length % AES_BLOCK_SIZE; //mod is required because of AES padding
        mod = AES_BLOCK_SIZE - mod;
        for (int i = 0; i < length + mod; i += AES_BLOCK_SIZE) // simple AES decryption
            AES_decrypt(data + i, data + i, &key_d);
        outfile.write((char *)data, length);
        outfile.close();
        printf("File was received \n");
    }
    else //not first neither last packet, decrypt and write to file
    {
        for (int i = 0; i < PACKETLEN; i += AES_BLOCK_SIZE)
            AES_decrypt(data + i, data + i, &key_d);
        outfile.write((char *)data, PACKETLEN);
    }
}

/* mypcap_handler() is a function that processes captured packets and determines whether it is ipv4 or ipv6 packet
   the function is called by pcap_loop()    */
void mypcap_handler(u_char *args, const struct pcap_pkthdr *header, const u_char *packet)
{
    unsigned char *packetData = (unsigned char *)packet + SIZE_ETHERNET_LINUX_CAPTURE + 20 + sizeof(struct icmphdr);
    if (strncmp((char *)packetData, "START:", 6) == 0)
    {
        IPSIZE = 20;
        receive_file(packet);
    }
    else if (strncmp((char *)packetData + 20, "START:", 6) == 0)
    {
        IPSIZE = 40;
        receive_file(packet);
    }
    else
    {
        receive_file(packet);
    }
}

/* The function opens interface "any" and starts sniffing icmp or icmp6 packets */
int server()
{
    char errbuf[PCAP_ERRBUF_SIZE]; // constant defined in pcap.h
    pcap_t *handle;                // packet capture handle
    pcap_if_t *alldev, *dev;       // a list of all input devices
    char const *devname = "any";   // a name of the device
    struct in_addr a, b;
    bpf_u_int32 netaddr;   // network address configured at the input device
    bpf_u_int32 mask;      // network mask of the input device
    struct bpf_program fp; // the compiled filter

    // open the input devices (interfaces) to sniff data
    if (pcap_findalldevs(&alldev, errbuf))
        err(1, "Can't open input device(s)");

    // list the available input devices
    printf("Available input devices are: ");
    for (dev = alldev; dev != NULL; dev = dev->next)
    {
        printf("%s ", dev->name);
    }
    printf("\n");

    // get IP address and mask of the sniffing interface
    if (pcap_lookupnet(devname, &netaddr, &mask, errbuf) == -1)
        err(1, "pcap_lookupnet() failed");

    a.s_addr = netaddr;
    printf("Opening interface \"%s\" with net address %s,", devname, inet_ntoa(a));
    b.s_addr = mask;
    printf("mask %s for listening...\n", inet_ntoa(b));

    // open the interface for live sniffing
    if ((handle = pcap_open_live(devname, BUFSIZ, 1, 1000, errbuf)) == NULL)
        err(1, "pcap_open_live() failed");

    // compile the filter
    if (pcap_compile(handle, &fp, "icmp or icmp6", 0, netaddr) == -1)
        err(1, "pcap_compile() failed");

    // set the filter to the packet capture handle
    if (pcap_setfilter(handle, &fp) == -1)
        err(1, "pcap_setfilter() failed");

    // read packets from the interface in the infinite loop (count == -1)
    // incoming packets are processed by function mypcap_handler()
    if (pcap_loop(handle, -1, mypcap_handler, NULL) == -1)
        err(1, "pcap_loop() failed");

    // close the capture device and deallocate resources
    pcap_close(handle);
    pcap_freealldevs(alldev);
    return 0;
}
