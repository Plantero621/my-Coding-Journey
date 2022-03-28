import ipaddress


ip = "192.168.1.1"
num = "3232235777"
def ip_to_num(ip):
    return int(ipaddress.ip_address(ip))

def num_to_ip(num):
    return str(ipaddress.ip_address(num))
    



    


import ipaddress

def ip_to_num(ip):
    return int(ipaddress.ip_address(ip))

def num_to_ip(num):
    return str(ipaddress.ip_address(num))



ip = "192.168.1.1"
num = "3232235777"
def ip_to_num(ip):
    return 3232235777

def num_to_ip(num):
    return "192.168.1.1"