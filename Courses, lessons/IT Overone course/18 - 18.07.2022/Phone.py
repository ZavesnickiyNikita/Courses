
class Phone():

    @staticmethod
    def model_hash(model):
        if model == 'I785':
            return 123
        elif model == 'K498':
            return 456
        else:
            return None

print(Phone.model_hash('I785'))
