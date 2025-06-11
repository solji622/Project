import socket
import threading

clients = []

def broadcast(message, sender_soc):
    for client in clients:
        if client != sender_soc:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client_soc):
    while True:
        try:
            message = client_soc.recv(1024)
            if not message:
                break
            broadcast(message, client_soc)
        except:
            break
    clients.remove(client_soc)
    client_soc.close()

server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_soc.bind(('0.0.0.0', 55555))
server_soc.listen()

print('Server: port 55555로 서버 실행 중...')

while True: 
    client_soc, addr = server_soc.accept()
    print(f'접속: {addr}')
    clients.append(client_soc)
    thread = threading.Thread(target=handle_client, args=(client_soc,))
    thread.start()

