import socketserver
from logic import Tracker
from db_logic import DataBaseRecoder


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class TrackingTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        tracker = Tracker(data=data.decode('utf-8'))
        result = tracker.process_data()
        try:
            data_base = DataBaseRecoder(number_of_participant=tracker.number_of_participant,
                                        link_id=tracker.link_id,
                                        number_of_group=tracker.number_of_group,
                                        time_for_db=tracker.time_for_db,
                                        )
            data_base.create_db()
            data_base.add_data()
            print('Message: ', result)
            self.request.sendall(bytes(result, encoding='utf-8'))
        except Exception:
            error = 'Не удалось внести запись в базу данных. Попробуйте ввести данные еще раз.'
            print(error)
            self.request.sendall(bytes(error, encoding='utf-8'))


if __name__ == '__main__':
    with ThreadingTCPServer(('127.0.0.1', 8888), TrackingTCPHandler) as server:
        server.serve_forever()
