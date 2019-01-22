#filename:host_ip.py (in chap12)
#funcion :convert the hostname to ip address


#end_pymotw_header

import socket
#import search_web_name


def show_many_host():
    print("\n Host name          ip_address")
    print("--------------------------------")
    for host in [ 'www.asus.com','www.python.org','hongkong','www.google.com' ]:
        try:
            ipaddr=socket.gethostbyname(host)
            print ('%15s     %s' % (host, ipaddr))
        except socket.error as msg:
            print ('%15s     erros is %s' % (host, msg))


def show_host_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print ("\nHost name: %s" % host_name)
    print ("IP address : %s" % ip_address)

if __name__ == '__main__':
    print("\nShow the host information")
    show_many_host()
    show_host_info()
