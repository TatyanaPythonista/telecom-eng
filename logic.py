class Tracker:

    def __init__(self, data):
        self.data = data
        self.number_of_participant = None
        self.link_id = None
        self.time = None
        self.number_of_group = None

    def process_data(self):
        self.data = self.data[:-2].split('x')
        self.number_of_participant = self.data[0]
        self.link_id = self.data[1]
        self.time = self.data[2][:-4]
        self.number_of_group = self.data[3]
        return f'Спортсмен, нагрудный номер {self.number_of_participant} прошёл отсечку {self.link_id} в {self.time}.'
