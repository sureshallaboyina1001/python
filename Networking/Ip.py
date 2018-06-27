import socket

host="www.yahoo.com"
try:
    addr=socket.gethostbyname(host)
    print("Ip Address="+addr)
except socket.gaierror:
    print("The website does not exits")
