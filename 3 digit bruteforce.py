import socket
import sys
import itertools
import os


for i in range(0,1):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('YOUR NC HOST', YOUR NC PORT)
	print >>sys.stderr, 'connecting to %s port %s' % server_address
	sock.connect(server_address)
	numbers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	y = ''
	for c in itertools.product(numbers, repeat=3):
   		pin = y+''.join(c)
		print >>sys.stderr, 'sending "%s"' % pin
		sock.send(pin)

		amount_received = 0
		amount_expected = len(pin)
	    	while amount_received < amount_expected:
			data = sock.recv(1024)
			amount_received += len(data)
			print >>sys.stderr, 'received "%s"' % data    


