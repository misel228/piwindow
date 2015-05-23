#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals
import demo
import pi3d


DISPLAY = pi3d.Display.create(x=0, y=0)
shader = pi3d.Shader("uv_flat")
CAMERA = pi3d.Camera(is_3d=False)
sprite = pi3d.ImageSprite("images/testbild_opt.png", shader, w=100.0, h=100.0, z=5.0)
mykeys = pi3d.Keyboard()
xloc = 100.0
yloc = 100.0

#read config

#loop
    #connect to server
    
    #loop
    while DISPLAY.loop_running():
    sprite.draw()
    sprite.position(xloc, yloc, 5.0)

        #data on socket?
            #read image/position
            #render image
    if mykeys.read() == 27:
        mykeys.close()
        DISPLAY.destroy()
        break

    #disconnect

  
