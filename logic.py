import logging

main_log = logging.getLogger('main')
main_log.setLevel(logging.DEBUG)
main_fh = logging.FileHandler("tracker.log", 'a', 'utf-8')
main_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
main_fh.setFormatter(main_formatter)
main_log.addHandler(main_fh)


class Tracker:

    def __init__(self, data):
        self.data = data
        self.number_of_participant = None
        self.link_id = None
        self.time = None
        self.time_for_db = None
        self.number_of_group = None

    def check_data(self):
        if len(self.number_of_participant) == 4 and len(self.link_id) == 2 and len(self.time_for_db) == 12 \
                and len(self.number_of_group) == 2:
            if self.number_of_participant.isdigit() and self.number_of_group.isdigit():
                return True

    def process_data(self):
        self.data = self.data.strip()
        try:
            self.number_of_participant, self.link_id, self.time_for_db, self.number_of_group = self.data.split(' ')
            self.time = self.time_for_db[:-4]
            if self.check_data():
                main_log.info(f'Данные {self.data} обработаны.')
                return f'Спортсмен, нагрудный номер {self.number_of_participant} прошёл отсечку ' \
                       f'{self.link_id} в {self.time}.'
            else:
                raise Exception
        except Exception:
            message_error = 'Ошибка в веденных данных'
            main_log.error(f'{message_error}. Введенные данные {self.data}')
            return message_error
