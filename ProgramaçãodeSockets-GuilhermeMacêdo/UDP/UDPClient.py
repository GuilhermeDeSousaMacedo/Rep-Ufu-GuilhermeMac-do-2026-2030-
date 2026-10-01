from socket import *

print("=" * 45)
print("{:^45}".format("Cliente UDP Uppercase"))
print("=" * 45, "\n")


serverName = 'localhost'
serverPort = 1208
clientSocket = socket(AF_INET,SOCK_DGRAM)

print(f"Escreva: 'Fechar Servidor' para sair do servidor\n")

while True:

    Message = input("Você: ")
    if Message.lower() == 'Fechar Servidor':
        break

message = input('\nInput lowercase sentance\n')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, severAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()