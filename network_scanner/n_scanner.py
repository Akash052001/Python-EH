# importing scapy

import scapy.all as scapy


def scan(ip):
    # creating arp packet
    arp_request = scapy.ARP(pdst=ip)

    # creating ether net frame to brodcast
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # combining arp_request into the ether net frame to create single packet
    arp_single_packet = broadcast / arp_request

    # sending the created packet (broadcasting the packet) using srp(send recieve packet
    # storing the returned list by srp in variables
    answered_list, unanswered_list = scapy.srp(arp_single_packet, timeout=1, verbose=False)
    # Extracting necessary data only in answered list
    print("IP address's" + "\t\t" + "Mac address's")
    print("---------------------------------------------")
    for element in answered_list:
        print("|" + element[1].psrc + "\t\t" + element[1].src + "   |")
        print("|___________________________________________|")


scan("172.20.8.1/24")
