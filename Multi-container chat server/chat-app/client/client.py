import socket
import time

HOST = 'chat_server'  # Docker Compose 서비스 이름
PORT = 12345

time.sleep(2)  # 서버가 먼저 뜨도록 대기

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello from client!')
    data = s.recv(1024)
    print('Received from server:', data.decode())
