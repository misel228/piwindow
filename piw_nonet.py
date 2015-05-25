#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals
import pi3d
import ConfigParser
from PIL import Image
import sys

#read config
Config = ConfigParser.ConfigParser()
Config.read("config.ini")

xloc  = int(Config.get("client",'x_offset'))
yloc  = int(Config.get("client",'y_offset'))


x_virtual = int(Config.get("client",'x_virtual'))
y_virtual = int(Config.get("client",'y_virtual'))

ifile = Config.get("client","default_image")
im = Image.open(ifile)
xsize,ysize = im.size
zindex = 5


DISPLAY = pi3d.Display.create(x=0, y=0)
DISPLAY.set_background(0,0,0,0) #black

xloc = xloc + (x_virtual - DISPLAY.width) / 2
yloc = yloc + (y_virtual - DISPLAY.height) / 2


##print("foo %d " % DISPLAY.width)
#sys.exit


shader = pi3d.Shader("uv_flat")
CAMERA = pi3d.Camera(is_3d=False)
mykeys = pi3d.Keyboard()
sprite = pi3d.ImageSprite(ifile, shader, w=xsize, h=ysize, z=zindex)

while DISPLAY.loop_running():
    sprite.position(xloc, yloc, zindex)
    sprite.draw()
    if mykeys.read() == 27:
	mykeys.close()
	DISPLAY.destroy()
	break

