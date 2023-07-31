import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.tela = ai_game.tela
        self.configuracoes = ai_game.configuracoes
        self.cor = self.configuracoes.bala_cor

        self.rect = pygame.Rect(0, 0, self.configuracoes.bala_largura, self.configuracoes.bala_altura)
        self.rect.midtop = ai_game.espaconave.local.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.configuracoes.velocidade
        self.rect.y = self.y
        

    def desenhar_bala(self):
        pygame.draw.rect(self.tela, self.cor, self.rect)