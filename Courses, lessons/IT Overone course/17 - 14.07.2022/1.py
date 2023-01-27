
class Phone:

    def __init__(self, color, model):
        self.color = color
        self.model = model

    def check_sim(self, mobile_operator):
        if self.model == 'I758' and mobile_operator == 'MTS':
            print('Your mobile operator is MTS')
    @staticmethod
    def model_hash(model):
        if model == 'I785':
            return 123
        elif model == 'K498':
            return 456
        else:
            return None

Phone.model_hash('I785')
my_phone = Phone('red', 'I785')
my_phone.check_sim('MTS')

my_phone = Phone('red', 'I758')
my_phone.check_sim('MTS')
