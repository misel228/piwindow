#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals
import pi3d
import ConfigParser
import socket
import sys

#read config
Config = ConfigParser.ConfigParser()
Config.read("config.ini")

name   = Config.get("client",'name')
server = Config.get("client",'server')
port   = int(Config.get("client",'port'))


xloc = int(Config.get("client",'x_offset'))
yloc = int(Config.get("client",'y_offset'))

xsize = 1280
ysize = 800
zindex = 5
image_file = "images/testbild_opt.png"



#loop
#connect to server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((server,port))
foo = s.recv(3)
print("%s" % foo.decode('ascii'))
s.close
sys.exit(0)



DISPLAY = pi3d.Display.create(x=0, y=0)
shader = pi3d.Shader("uv_flat")
CAMERA = pi3d.Camera(is_3d=False)
mykeys = pi3d.Keyboard()
sprite = pi3d.ImageSprite(image_file, shader, w=xsize, h=ysize, z=zindex)




#loop
while DISPLAY.loop_running():
    #data on socket?
	#read image(size)/position
	#sprite = pi3d.ImageSprite(image_file, shader, w=xsize, h=ysize, z=zindex)
    sprite.position(xloc, yloc, zindex)
	#render image
    sprite.draw()
    if mykeys.read() == 27:
	mykeys.close()
	DISPLAY.destroy()
	break
	#disconnect

