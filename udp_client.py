import ConfigParser
import socket
import sys

class _GetchUnix:
	def __init__(self):
		import tty, sys

	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

#read config
Config = ConfigParser.ConfigParser()
Config.read("config.ini")

address_data = Config.get("server",'addresses')
port    = int(Config.get("client",'port'))

addresses = address_data.split(',')
print addresses

getch = _GetchUnix()

x = 0
y = 0

while 1:
	foo = getch()
	if foo == 'q':
		print "exit"
		sys.exit()
	elif foo == 'w':
		y = y - 1
	elif foo == 's':
		y = y + 1
	elif foo == 'a':
		x = x - 1
	elif foo == 'd':
		x = x + 1
	coords = "X%010dY%010d" % (x,y)
	print coords
	for address in addresses:
		print address
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(coords, (address, port))

