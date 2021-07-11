import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('127.0.0.1', 8888))
    message = input('Введите данные: ')
    sock.send(bytes(message, encoding='utf-8'))

    while True: # Заходим в бесконечный цикл и пытаемся принять соединение
        data = sock.recv(1024)
        print('Message: ', data.decode('utf-8'))
