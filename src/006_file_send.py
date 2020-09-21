import sys
import socket

def main():
	if len(sys.argv) is not 3:
		print("usage: %s [ip adress][input filename] " % sys.argv[0] )
		return(-1)

	#make a socket
	#socket is a combination of network address and port identifier
	#A connection is the connection between two socket
	#AF_INET is one of the address family which means IPv4
	#Socket Type: SOCK_STREAM = TCP, SOCK_DGRAM = UDP
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		# specify ip address and port
		#no need if don't want to bind any specific local endpoint to the connection
		#s.bind(('127.0.0.1', 50007))
		
		#connect to only one
		s.connect((sys.argv[1], 11111))
		input_file = open(sys.argv[2], 'rb')
		line = input_file.read()
		while line:
			s.send(line)
			line = input_file.read()
		input_file.close()

if __name__ == '__main__':
	main()


