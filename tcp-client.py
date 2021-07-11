import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))
message = input('Введите данные: ')
sock.send(bytes(message, encoding='utf-8'))
sock.close()
