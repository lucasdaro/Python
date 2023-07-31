import pygame
from pygame.sprite import Sprite

class Alienigena(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.tela = ai_game.tela
        self.settings = ai_game.configuracoes

        self.image = pygame.image.load('imagens/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.tela.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)