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
            if self.number_of_participant.isdigit() and self.link_id.isdigit() and self.number_of_group.isdigit():
                return True

    def process_data(self):
        try:
            self.number_of_participant, self.link_id, self.time_for_db, self.number_of_group = self.data[:-2].split('x')
            self.time = self.time_for_db[:-4]
            if self.check_data():
                return f'Спортсмен, нагрудный номер {self.number_of_participant} прошёл отсечку ' \
                       f'{self.link_id} в {self.time}.'
            else:
                raise Exception
        except Exception:
            message_error = 'Ошибка в веденных данных'
            return message_error

# BBBBxNNxHH:MM:SS.zhqxGGCR
# 0001x00x11:40:30.000x55CR
