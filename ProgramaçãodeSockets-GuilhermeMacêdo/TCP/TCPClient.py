from socket import *

print("=" * 45)
print("{:^45}".format("Cliente UDP Uppercase"))
print("=" * 45, "\n")

serverName = '10.0.99.150'
severPort = 1208
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, severPort))
sentence = input('Coloque a sentença em minúsculo: \n')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('Servidor: ', modifiedSentence.decode())
clientSocket.close()