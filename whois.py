import socket, sys
cx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cx.connect(('200.160.2.3', 43))
cx.send('tim.com.br\r\n')
result = cx.recv(1024)

print(result)