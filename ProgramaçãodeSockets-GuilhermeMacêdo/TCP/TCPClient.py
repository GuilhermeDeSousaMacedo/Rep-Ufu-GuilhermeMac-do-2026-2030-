from socket import *

serverName = 'guilherme-ufu'
severPort = 1208
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, severPort))
sentence = input('Input lowercase sentence: \n')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()