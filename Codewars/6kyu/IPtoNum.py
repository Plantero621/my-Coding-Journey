from base64 import b32encode
import ipaddress


ip = "192.168.1.1"
num = "3232235777"
def ip_to_num(ip):
    b1n = ip.split(".")
    b2n =""
    b3n = []
    b4n = 0
    for i in b1n:
        temp=(bin(int(i))[2:])
        while len(temp) < 8:
            temp = "".join(("0","{}")).format(temp)
        print(temp)
        b2n = "".join((b2n,"{}")).format(temp)
    ress = int(b2n, 10)
    print(ress)

def num_to_ip(num):
    return int(ipaddress.ip_address(ip))

