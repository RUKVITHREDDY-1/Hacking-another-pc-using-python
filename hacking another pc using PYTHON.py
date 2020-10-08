import socket
import xmlrpc.client


HOST='0.0.0.0' #means server will bind to any ip
PORT=1234

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates serveers TCP socket
server_socket.setsockopt(xmlrpc.client.ServerProxy,socket.so_REUSEADDR,1)#prevents fromgetttikng timeout issues
server_socket.bind((HOST,PORT))
server_socket.listen(5) #five connections max at queue sT TIME

 
client_socket,(client_ip, client_port) = server_socket.accept()

while True:

     command = raw_input(">")
     client_socket.send(command)

     if(command == "quit"):
         break

data = client_socket.recv(1024)
print (data)

client_socket.close()

