import socketserver
from logic import Tracker
from db_logic import DataBaseRecoder
import logging

main_log = logging.getLogger('main')
main_log.setLevel(logging.DEBUG)
main_fh = logging.FileHandler("tracker.log", 'a', 'utf-8')
main_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
main_fh.setFormatter(main_formatter)
main_log.addHandler(main_fh)


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class TrackingTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        main_log.info(f'На сервер поступили данные {data.decode("utf-8")}')
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
            main_log.info(f'Данные {tracker.number_of_participant} {tracker.link_id} '
                          f'{tracker.number_of_group} {tracker.time_for_db} записаны в базу данных.')
            self.request.sendall(bytes(result, encoding='utf-8'))
            main_log.info(f'Клиенту отправлено сообщение {result}')
        except Exception:
            error = 'Не удалось внести запись в базу данных. Попробуйте ввести данные еще раз.'
            main_log.error(f'Данные {tracker.number_of_participant} {tracker.link_id} '
                          f'{tracker.number_of_group} {tracker.time_for_db} не удалось записать в базу данных.')
            self.request.sendall(bytes(error, encoding='utf-8'))


if __name__ == '__main__':
    with ThreadingTCPServer(('127.0.0.1', 8888), TrackingTCPHandler) as server:
        server.serve_forever()
