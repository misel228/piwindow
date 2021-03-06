#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals
import pi3d
import pi3d
import ConfigParser
from PIL import Image
import sys
import socket
import time

pi3d.util.Log.set_logs('DEBUG', '/tmp/piwindow.log', "%(asctime)s %(levelname)s: %(name)s: %(message)s")

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


LOGGER = pi3d.util.Log.logger(__name__)


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

print("set up display")
xsize,ysize = im.size
zindex = 5

DISPLAY = pi3d.Display.create(x=0, y=0)
DISPLAY.set_background(0,0,0,0) #black

xloc = xloc + (x_virtual - DISPLAY.width) / 2
yloc = yloc - (y_virtual - DISPLAY.height) / 2

print("set up shader")
shader = pi3d.Shader("uv_flat")

print("set up Camera")
CAMERA = pi3d.Camera(is_3d=False)

print("set up keyboard")
mykeys = pi3d.Keyboard()

print("set up sprite")
try:
	sprite = pi3d.ImageSprite(ifile, shader, w=xsize, h=ysize, z=zindex)
except:
	print("Error")
	time.sleep(10)

LOGGER.info("foobar")

print("start loop")

coords = [0,0]

while DISPLAY.loop_running():
	sprite.position(xloc+coords[0], yloc+coords[1], zindex)
	sprite.draw()
	if mykeys.read() == 27:
		mykeys.close()
		DISPLAY.destroy()
		break

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

print("end")

s.close()
