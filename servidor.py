import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ip e porta 
server.bind(("localhost",8888))

#inicia o servidor
server.listen()
client, address = server.accept()

sair = False

while not sair:
    #recebe a mensagem
    msg = client.recv(1024).decode('utf-8')
    if msg.lower() == "exit":
        sair = True
    else:
        print(msg)
    texto = input('Digite a sua mensagem para o cliente: ')
    client.send(texto.encode('utf-8'))