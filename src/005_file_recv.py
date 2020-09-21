import sys
import socket

def main():
	if len(sys.argv) is not 2:
		print("usage: %s [to filename] " % sys.argv[0] )
		return -1

	output_file = open(sys.argv[1], "w+")

	#make a socket
	#socket is a combination of network address and port identifier
	#A connection is the connection between two socket
	#AF_INET is one of the address family which means IPv4
	#Socket Type: SOCK_STREAM = TCP, SOCK_DGRAM = UDP
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		# specify ip address and port
		#no need if don't want to bind any specific local endpoint to the connection
		#s.bind(('127.0.0.1', 50007))
		s.bind(('', 11111))
		#only one connection at a time
		s.listen(1)

		#wait until there is a connection request
		while True:
			#insert the descriptor of the socket into conn, addr if there is a connection
			(conn, addr) = s.accept() 
			with conn:
				data = conn.recv(1024)
				while (data):
					output_file.write(data.decode())
					data = conn.recv(1024)
				output_file.close()
			break

if __name__ == '__main__':
	main()

