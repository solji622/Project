import socket
import threading

def receive_messages(sock):
    while True:
        try: 
            message = sock.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            break

name = input('닉네임 입력: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('chat_server', 55555))

threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

while True:
    try:
        msg = input()
        if msg.lower() == 'exit':
            break
        full_msg = f'{name}: {msg}'
        client.sendall(full_msg.encode())
    except:
        break
client.close()