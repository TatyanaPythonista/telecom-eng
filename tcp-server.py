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
