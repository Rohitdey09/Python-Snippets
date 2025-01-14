##Finding hostname and IP adress with python
import socket
def get_Host_name_IP():
    try:
        hostname_name = socket.gethostname()
        host_ip = socket.gethostbyname(hostname_name)
        print("Hostname:",hostname_name)
        print("IP:",host_ip)
    except:
        print("Unable to get hostname and IP")
get_Host_name_IP()           
        
        