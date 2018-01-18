import socket
host=socket.gethostname()
port=1234
server_socket = socket.socket()
server_socket.bind((host,port))
server_socket.listen(2)

con,addr = server_socket.accept()

print("file is accepted from address:",addr)
msg=con.recv(1024).decode()
print("file name is:",msg)
f=open(msg)
l=f.read()
con.send(l.encode())
con.close()
