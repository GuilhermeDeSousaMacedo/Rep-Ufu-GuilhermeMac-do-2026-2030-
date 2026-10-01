from socket import *

print("=" * 45)
print("{:^45}".format("Servidor UDP Uppercase"))
print("=" * 45, "\n")

serverPort = 1208
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort)) 

print('Servidor em execução...')
message, clientAddress = serverSocket.recvfrom(2048)
modifiedMessage = message.decode().upper()
serverSocket.sendto(modifiedMessage.encode(), clientAddress)