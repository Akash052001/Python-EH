import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface for operation eg,wlan0,eth0 etc;")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address to change to")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[=] Maybe you forgot to enter interface (--help for help)")
    elif not options.new_mac:
        parser.error("[=] Maybe you forgot to enter mac address (--help for help)")
    else:
        return options


def change_mac(interface, new_mac):
    print("\n[+] Changing mac address for " + interface + " to new mac " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def curunt_mac(interface):
    result = subprocess.check_output(["ifconfig", interface])
    s_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))

    if s_mac:
        return s_mac.group(0)
    else:
        print("[=] Could not read mac address")


options = get_arguments()
current_mac = curunt_mac(options.interface)
print("Current mac :", str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = curunt_mac(options.interface)
if current_mac == options.new_mac:
    print(">> Successfully Changed mac address to: ", current_mac)
else:
    print("[=] Unsuccessful")
