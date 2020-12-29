from socket import *
serverName = '127.0.0.1'
serverHost = 12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
message=input("input lowercase sentence : ")
clientSocket.sendto(message.encode(),(serverName,serverHost))
modified,serverAddress=clientSocket.recvfrom(2048)
print(modified.decode())
clientSocket.close()