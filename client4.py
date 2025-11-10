import socket
from pythonping import ping
s=socket.socket() 
s.bind(('localhost', 8000))
s.listen(5)
c, addr = s.accept()
while True:
	hostname = c.recv(1024).decode()
	try:
		c.send(str(ping(hostname, verbose=False)).encode())
	except KeyError:
		c.send("Not Found".encode())
