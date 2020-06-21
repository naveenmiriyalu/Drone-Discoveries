#Need to add more features 

import socket

#Create a socket through UDP 

tello_ip='192.168.10.1'
tello_port=8889
tello_address=(tello_ip,tello_port)

local_host=''
local_port=9000
local_addr =(local_host,local_port)

try:
	client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.err as err:
	print("Tried to open socket . Failure %s" %(err) )

# add error catching code for client_sock
client_sock.connect(tello_address)
client_sock.bind(local_addr)
msg="command"
msg = msg.encode(encoding="utf-8")

client_sock.sendto(msg,tello_address)
data,server = client_sock.recvfrom(2000)
print("data received= ",data)

print("Closing the client socket")
client_sock.close();




