# import socket
# from logic import Tracker
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:  # передаем в конструктор SOCK_STREAM чтобы использовать tcp протакол
#     sock.bind(('127.0.0.1', 8888)) # связываемся, резервируем порт
#     sock.listen(5) # размер очереди, сколько соединений мы хотим слушать
#
#     while True: # Заходим в бесконечный цикл и пытаемся принять соединение
#         client, addr = sock.accept() # accept смотрит в очереди есть ли какие-нибудь клиенты
#         client.setblocking(True)
#         data = client.recv(1024)
#         tracker = Tracker(data=data.decode('utf-8'))
#         result = tracker.process_data()
#         client.send(bytes(result, encoding='utf-8'))
#         print('Message: ', result)

import socketserver
from logic import Tracker


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class TrackingTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        tracker = Tracker(data=data.decode('utf-8'))
        result = tracker.process_data()
        print('Message: ', result)
        self.request.sendall(bytes(result, encoding='utf-8'))


if __name__ == '__main__':
    with ThreadingTCPServer(('127.0.0.1', 8888), TrackingTCPHandler) as server:
        server.serve_forever()
