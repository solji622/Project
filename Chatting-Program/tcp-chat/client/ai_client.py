import socket
import threading
import time
from ai_model import get_ai_reply

name = input('AI 이름 : ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('chat_server', 55555))

def receive_and_respond(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message.strip() or message.startswith(name + ":"):
                continue
            reply = get_ai_reply(message)
        
            full_msg = f"{name} : {reply}"
            time.sleep(1)
            sock.sendall(full_msg.encode())
        except Exception as e:
            print("error:", e)
            break

client.sendall(f"{name}: 안녕? 반가워!".encode())

threading.Thread(target=receive_and_respond, args=(client,), daemon=True).start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break

client.close()