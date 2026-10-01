import sys
from socket import *

print("=" * 45)
print("{:^45}".format("Cliente UDP Real -> Yuan"))
print("=" * 45, "\n")

# Uso: python UDPClient.py [ip_do_servidor] [porta]
serverName = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
serverPort = int(sys.argv[2]) if len(sys.argv) > 2 else 1208

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(3)  # UDP não garante entrega: não ficar esperando para sempre

print(f'Conectando a {serverName}:{serverPort}')
print('Digite "sair" para encerrar.')

try:
    while True:
        message = input('\nValor em reais (R$): ').strip()
        if message.lower() == 'sair':
            break
        if not message:
            continue

        clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            print('Servidor:', modifiedMessage.decode('utf-8'))
        except timeout:
            print('Sem resposta do servidor (timeout). Verifique IP, porta e firewall.')
except KeyboardInterrupt:
    print()
finally:
    clientSocket.close()