from random import randint

class Dado:
    def __init__(self, tipo_do_dado = 6):
        self.tipo_do_dado = tipo_do_dado

    def jogar(self):
        return randint(1, self.tipo_do_dado)
