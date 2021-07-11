import socket
from logic import Tracker

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # передаем в конструктор SOCK_STREAM чтобы использовать tcp протакол
sock.bind(('127.0.0.1', 8888)) # связываемся, резервируем порт
sock.listen(5) # размер очереди, сколько соединений мы хотим слушать

while True: # Заходим в бесконечный цикл и пытаемся принять соединение
    try:
        client, addr = sock.accept() # accept смотрит в очереди есть ли какие-нибудь клиенты
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        data = client.recv(1024)
        tracker = Tracker(data=data.decode('utf-8'))
        result = tracker.process_data()
        client.close()
        print('Message: ', result)
