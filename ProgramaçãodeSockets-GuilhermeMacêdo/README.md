# Trabalho avaliativo do segundo semestre do curso de Cibersegurança+laboratório do Professor Renato em sala de aula 09-09-2026 X 02-10-2026:
### A seguir irei documentar minha experiência em programação de Sockets seguindo os protocolos Tcp e Udp respectivamente mostrando suas funcionalidades, aplicações e funcionalidade no servidor dedicado da Ufu do curso de Cibersegurança tendo em base o Livro de [[Análise do Livro (Redes de computadores e a Internet ,Kurose [Sprint]]] e Aula de laboratório proposta em sala pelo professor Renato e ao mesmo tempo realizando a atividade avaliativa do curso de Cibersegurança.

### Nota:
Apesar da atividade ter um caráter prático eu considero que seu valor se baseia mais no teórico devido a base em "Redes" que preciso entender para conseguir explicar suas características e aplicações além, de informações correlacionadas na camada de aplicação.
# O Trabalho:
O trabalho é bem simples constituindo-se de dois protocolos diferentes utilizados na programação de sockets no qual um texto minúsculo(lower.case) é enviado para o servidor, analisado e devolvido em Maiúsculo(upper.case) demonstrando assim a capacidade de comunicação entre dois dispositivos diferentes, que apesar da mesma aplicação(mesma função) possuem características distintas ao realizarem a tarefa de acordo com o respectivo protocolo

## Protocolos utilizados:
### UDP (User Datagram Protocol)

O UDP é um protocolo da camada de transporte **sem conexão** e **não confiável**. Ele pega os dados da aplicação, adiciona um cabeçalho mínimo (portas de origem e destino, tamanho e checksum, 8 bytes no total) e envia o datagrama, sem estabelecer conexão antes e sem confirmar se chegou.

**Características:**

- Sem handshake: o envio começa imediatamente.
- Sem garantia de entrega, de ordem ou de ausência de duplicatas.
- Sem controle de fluxo nem de congestionamento.
- Cabeçalho pequeno e baixa latência.
- Cada datagrama é independente, com limites de mensagem preservados.

**Quando usar:** quando velocidade importa mais que confiabilidade, ou quando a aplicação cuida da confiabilidade por conta própria. Exemplos: DNS, streaming de áudio e vídeo, VoIP, jogos online, DHCP e QUIC (que roda sobre UDP).

### TCP (Transmission Control Protocol)

O TCP é um protocolo **orientado a conexão** e **confiável**. Antes de trocar dados, os dois lados estabelecem uma conexão por meio do **three-way handshake** (SYN → SYN-ACK → ACK). Depois disso, os dados trafegam como um **fluxo contínuo de bytes**, e não como mensagens separadas.

**Características:**

- **Entrega confiável:** cada segmento recebido é confirmado por ACK, e o que não é confirmado é retransmitido.
- **Ordenação:** números de sequência garantem que os dados cheguem na ordem certa e sem duplicatas.
- **Controle de fluxo:** a janela de recepção impede que o emissor sobrecarregue o receptor.
- **Controle de congestionamento:** o TCP reduz a taxa quando percebe congestionamento na rede.
- **Encerramento ordenado:** a conexão é fechada com troca de FIN/ACK.
- Cabeçalho maior (mínimo de 20 bytes) e mais overhead.

**Quando usar:** quando perder ou embaralhar dados não é aceitável. Exemplos: HTTP/HTTPS, e-mail (SMTP, IMAP), SSH, FTP e transferência de arquivos em geral.
