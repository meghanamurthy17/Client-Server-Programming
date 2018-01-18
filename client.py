import socket
host = socket.gethostname()
port = 1234
client_socket = socket.socket()
client_socket.connect((host,port))
name=input("enter name of file:")
client_socket.send(name.encode())
msg=client_socket.recv(1024).decode()
print("msg:",msg)
client_socket.close()