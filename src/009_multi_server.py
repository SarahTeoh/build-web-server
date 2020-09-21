import sys
import socket
import _thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 11111))
s.listen(100)
list_of_clients = []

#TODO: exit program when client ends the connection
def connect(conn, addr):
	while True:
			try:
				received = conn.recv(1024)
				if received:
					received_msg = received
					print(received_msg.decode())
					broadcast(received_msg, conn)
				else:
					remove(conn)
					
			except:
				continue

def broadcast(message, connection):
	for client in list_of_clients:
		if client!=conenction:
			try:
				client.send(message)
			except:
				client.close()
				remove(client)


def remove(connection):
	if connection in list_of_clients:
		list_of_clients.remove(connection)


while True:
	(conn, addr) = s.accept() 
	list_of_clients.append(conn)
	_thread.start_new_thread(connect, (conn, addr)) 	#second argument of this function must be tuple

conn.close()
s.close()

	

