from socket import *

serverName = 'localhost'
serverPort = 1228
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input('\nInput lowercase sentance\n')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, severAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()