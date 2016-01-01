import ConfigParser
import socket
import sys
import time



def coords_str2int(coords):
	if len(coords) != 22:
		return False
	x = coords[0]
	if x != 'X':
		return False
	y = coords[11]
	if y != 'Y':
		return false
	x_value = coords[1:11]
	y_value = coords[12:22]
	int_coords = (int(x_value), int(y_value))
	return int_coords


#read config
Config = ConfigParser.ConfigParser()
Config.read("config.ini")

address = Config.get("client",'address')
port    = int(Config.get("client",'port'))

# Datagram (udp) socket
try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket created'
except socket.error, msg :
	print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

# Bind socket to local host and port
try:
	s.bind((address, port))
	s.setblocking(0)
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	
print 'Socket bind complete'

#now keep talking with the client
while 1:
	try:
		# receive data from client (data, addr)
		d = s.recvfrom(1024)
		data = d[0]
		addr = d[1]
		
		if not data: 
			continue
		
		print "#" + data.strip() + "#"
		coords = coords_str2int(data.strip())
		
		if coords:
			print coords



	except:
		f = 'bar' # NOP


s.close()
