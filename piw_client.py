#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals
import pi3d
import ConfigParser
from PIL import Image
import sys
import socket

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

address = Config.get("client","address")
port = int(Config.get("client","port"))

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print("Socket created")
except socket.error, msg:
	print("Failed to create socket. Error Code : " + str(msg[0]) + " Message " + msg[1])
	sys.exit()

# Bind socket to local host and port
try:
	s.bind((address, port))
	s.setblocking(0)
except socket.error , msg:
	print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
	
print('Socket bind complete')



xloc  = int(Config.get("client",'x_offset'))
yloc  = int(Config.get("client",'y_offset'))


x_virtual = int(Config.get("client",'x_virtual'))
y_virtual = int(Config.get("client",'y_virtual'))

ifile = Config.get("client","default_image")
try:
	im = Image.open(ifile)
except:
	print("Could not open file "+ifile)
	sys.exit()


xsize,ysize = im.size
zindex = 5

DISPLAY = pi3d.Display.create(x=0, y=0)
DISPLAY.set_background(0,0,0,0) #black

xloc = xloc + (x_virtual - DISPLAY.width) / 2
yloc = yloc - (y_virtual - DISPLAY.height) / 2



shader = pi3d.Shader("uv_flat")
CAMERA = pi3d.Camera(is_3d=False)
mykeys = pi3d.Keyboard()
sprite = pi3d.ImageSprite(ifile, shader, w=xsize, h=ysize, z=zindex)

while DISPLAY.loop_running():
	try:
		# receive data from client (data, addr)
		d = s.recvfrom(1024)
		data = d[0]
		addr = d[1]
		if not data: 
			continue
		coords = coords_str2int(data.strip())
	except:
		f = 'bar' # NOOP

	sprite.position(xloc+coords[0], yloc+coords[1], zindex)
	sprite.draw()
	if mykeys.read() == 27:
		mykeys.close()
		DISPLAY.destroy()
		break

s.close()
