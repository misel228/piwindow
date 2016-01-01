#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals
import pi3d
import ConfigParser
import sys

DISPLAY = pi3d.Display.create(x=0, y=0)
shader = pi3d.Shader("uv_flat")
CAMERA = pi3d.Camera(is_3d=False)
mykeys = pi3d.Keyboard()


#read config
Config = ConfigParser.ConfigParser()
Config.read("config.ini")

name   = ConfigSectionMap("client")['name']
server = ConfigSectionMap("client")['server']
port   = ConfigSectionMap("client")['port']


xloc = ConfigSectionMap("client")['x_offset']
yloc = ConfigSectionMap("client")['y_offset']
image_file = ConfigSectionMap("client")['default_file_name']


from PIL import Image
im=Image.open(image_file)
im.size # (width,height) tuple

xsize = 1280
ysize = 800
zindex = 5
sys.exit


sprite = pi3d.ImageSprite(image_file, shader, w=xsize, h=ysize, z=zindex)


#loop
while DISPLAY.loop_running():
    #data on socket?
	#read image(size)/position
	#sprite = pi3d.ImageSprite(image_file, shader, w=xsize, h=ysize, z=zindex)
	#sprite.position(xloc, yloc, zindex)
	#render image
    #sprite.draw()
    if mykeys.read() == 27:
	mykeys.close()
	DISPLAY.destroy()
	break
	#disconnect

