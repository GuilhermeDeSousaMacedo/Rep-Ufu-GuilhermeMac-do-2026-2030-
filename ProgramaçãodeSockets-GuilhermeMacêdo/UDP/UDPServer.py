from socket import *
from math import isfinite

TAXA_REAL_YUAN = 0.78  # 1 real = 0,78 yuan


def converter_real_para_yuan(valor_reais):
    """Recebe um valor em reais e devolve o equivalente em yuan."""
    return valor_reais * TAXA_REAL_YUAN


print("=" * 45)
print("{:^45}".format("Servidor UDP Real -> Yuan"))
print("=" * 45, "\n")

serverPort = 1208
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))  # '' = escuta em todas as interfaces

print('Servidor em execução na porta', serverPort, '...')

try:
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        texto = message.decode('utf-8').strip().replace(',', '.')  # aceita 10,50

        try:
            reais = float(texto)
            if not isfinite(reais) or reais < 0:
                raise ValueError
            yuan = converter_real_para_yuan(reais)
            resposta = f'R$ {reais:.2f} = ¥ {yuan:.2f} (taxa: {TAXA_REAL_YUAN})'
        except ValueError:
            resposta = 'Erro: envie um valor numérico positivo (ex: 100 ou 10,50)'

        print(f'{clientAddress[0]}:{clientAddress[1]} enviou "{texto}" -> {resposta}')
        serverSocket.sendto(resposta.encode('utf-8'), clientAddress)

except KeyboardInterrupt:
    print('\nServidor encerrado.')
finally:
    serverSocket.close()
