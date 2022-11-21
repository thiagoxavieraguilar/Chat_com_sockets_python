import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#conecta ao servidor
client.connect(("localhost",8888))

sair = False
print('digite "exit" para finalizar o chatbox')


while not sair:
    texto = input('Digite a sua mensagem para o servidor: ')
    client.send(texto.encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if texto.lower() == "exit" or msg.lower() == "exit" :
        sair = True
    else:
        print(msg)

client.close()