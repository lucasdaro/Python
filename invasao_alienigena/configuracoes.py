class Configuracoes:
    """ ARMAZENAR CONFIGURAÇÕES DO JOGO """
    def __init__(self):
        #CONFIGURAÇÕES DA TELA
        self.largura_da_tela = 1600
        self.altura_da_tela = 900
        self.fundo_da_tela = (230, 230, 230)
        self.velocidade = 2.5
        self.bala_velocidade = 2.0
        self.bala_largura = 3
        self.bala_altura = 15
        self.bala_cor = (255,127,80)
        self.bala_quantidade = 5
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1