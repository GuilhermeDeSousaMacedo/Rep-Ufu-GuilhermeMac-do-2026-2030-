# Trabalho avaliativo do segundo semestre do curso de Cibersegurança+Laboratório do Professor Renato em sala de aula entre 09-09-2026 E 02-10-2026:
### A seguir irei documentar minha experiência em programação de Sockets seguindo os protocolos Tcp(Transmission Control Protocol) e Udp(User Datagram Protocol) respectivamente mostrando suas funcionalidades, aplicações e funcionalidade no servidor dedicado da Ufu do curso de Cibersegurança tendo em base o Livro de [Análise do Livro (Redes de computadores e a Internet ,Kurose [Sprint]] e Aula de laboratório proposta em sala pelo professor Renato e ao mesmo tempo realizando a atividade avaliativa do curso de Cibersegurança.

### Nota:
Apesar da atividade ter um caráter prático eu considero que seu valor se baseia mais no teórico devido a base em "Redes" que preciso entender para conseguir explicar suas características e aplicações além de informações correlacionadas na camada de aplicação.
# O Trabalho:
O trabalho é bem simples constituindo-se de dois protocolos e duas aplicações diferentes utilizados na programação de sockets no qual um texto minúsculo(lower.case) é enviado para o servidor, analisado e devolvido em Maiúsculo(upper.case) demonstrando assim a capacidade de comunicação entre dois dispositivos diferentes e o outro a conversão do Real(Moeda Brasileira) para Yuan(Moeda Chinesa) ao enviar o valor o servidor analisa e devolve a partir de uma operação o valor igualitário com a comparação Real x Yuan 
# Execução do trabalho:
Dentro de uma comand line faça os respectivos comandos:
1. ssh guilherme.sousa@10.0.9.170(ip aleatório para proteção de servidor
2. Aplicar senha requisitada para o acesso do servidor de cibersegurança da UFU
3. Python3 TCPServer.py para o acesso ao servidor TCP ou Python3 UDPServer.py(de acordo com a aplicação escolhida)
4. Run python TCPClient.py ou UDPServer.py(de acordo com a aplicação escolhida)
## Protocolos utilizados:
### UDP (User Datagram Protocol)

O UDP é um protocolo da camada de transporte **sem conexão** e **não confiável**. Ele pega os dados da aplicação, adiciona um cabeçalho mínimo (portas de origem e destino, tamanho e checksum, 8 bytes no total) e envia o datagrama, sem estabelecer conexão antes e sem confirmar se chegou.

**Características:**

- Sem handshake: o envio começa imediatamente.
- Sem garantia de entrega, de ordem ou de ausência de duplicatas.
- Sem controle de fluxo nem de congestionamento.
- Cabeçalho pequeno e baixa latência.
- Cada datagrama é independente, com limites de mensagem preservados.

**Quando usar:** quando velocidade importa mais que confiabilidade, ou quando a aplicação cuida da confiabilidade por conta própria. Exemplos: DNS (Domain Name System, ou Sistema de Nomes de Domínio), streaming de áudio e vídeo, VoIP (Voice over Internet Protocol, ou Voz sobre Protocolo de Internet), jogos online, DHCP (Dynamic Host Configuration Protocol, ou Protocolo de Configuração Dinâmica de Host) e QUIC (Quick UDP Internet Connections, ou Conexões de Internet UDP Rápidas) que roda sobre UDP (User Datagram Protocol, ou Protocolo de Datagrama de Usuário).

### TCP (Transmission Control Protocol)
O TCP (Transmission Control Protocol, ou Protocolo de Controle de Transmissão) é um protocolo orientado a conexão e confiável. Antes de trocar dados, os dois lados estabelecem uma conexão por meio do three-way handshake (SYN (Synchronize, ou Sincronizar) → SYN-ACK (Synchronize-Acknowledge, ou Sincronizar-Confirmar) → ACK (Acknowledgment, ou Confirmação)). Depois disso, os dados trafegam como um fluxo contínuo de bytes, e não como mensagens separadas.

**Características:**

- **Entrega confiável:** cada segmento recebido é confirmado por ACK, e o que não é confirmado é retransmitido.
- **Ordenação:** números de sequência garantem que os dados cheguem na ordem certa e sem duplicatas.
- **Controle de fluxo:** a janela de recepção impede que o emissor sobrecarregue o receptor.
- **Controle de congestionamento:** o TCP reduz a taxa quando percebe congestionamento na rede.
- **Encerramento ordenado:** a conexão é fechada com troca de FIN/ACK.
- Cabeçalho maior (mínimo de 20 bytes) e mais overhead.

**Quando usar: quando perder ou embaralhar dados não é aceitável. Exemplos: HTTP (Hypertext Transfer Protocol, ou Protocolo de Transferência de Hipertexto)/HTTPS (Hypertext Transfer Protocol Secure, ou Protocolo de Transferência de Hipertexto Seguro), e-mail (SMTP (Simple Mail Transfer Protocol, ou Protocolo Simples de Transferência de Correio), IMAP (Internet Message Access Protocol, ou Protocolo de Acesso a Mensagens da Internet)), SSH (Secure Shell, ou Shell Seguro), FTP (File Transfer Protocol, ou Protocolo de Transferência de Arquivos) e transferência de arquivos em geral.**
