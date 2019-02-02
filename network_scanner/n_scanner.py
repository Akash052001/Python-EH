# importing scapy
# importing optparse

import scapy.all as scapy
import optparse as opt


def get_arguments():
    parser = opt.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target Ip range")
    (options, arguments) = parser.parse_args()
    return options


def scan(ip):
    # creating arp packet
    arp_request = scapy.ARP(pdst=ip)

    # creating ether net frame to brodcast
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # combining arp_request into the ether net frame to create single packet
    arp_single_packet = broadcast / arp_request

    # sending the created packet (broadcasting the packet) using srp(send recieve packet
    # storing the returned list by srp in variables
    answered_list = scapy.srp(arp_single_packet, timeout=1, verbose=False)[0]
    # Extracting necessary data only in answered list and storing in list of dictionary
    scan_result = []

    for element in answered_list:
        scan_dict = {"ip": element[1].psrc, "mac": element[1].src}
        scan_result.append(scan_dict)

    return scan_result


def result_print(scan_result):
    print("IP address's" + "\t\t" + "Mac address's")
    print("---------------------------------------------")
    for each in scan_result:
        print("|" + each["ip"] + "\t\t" + each["mac"] + "   |")
        print("|___________________________________________|")


# function call's

option = get_arguments()
result = scan(option.target)
result_print(result)
