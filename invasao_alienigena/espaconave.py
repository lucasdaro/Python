import pygame

class EspacoNave:
    def __init__(self, ai_game):
        self.tela = ai_game.tela
        self.rect = ai_game.tela.get_rect()
        self.configuracoes = ai_game.configuracoes

        self.imagem = pygame.image.load('imagens/ship.bmp')
        self.local = self.imagem.get_rect()

        self.local.midbottom = self.rect.midbottom
        self.x = float(self.local.x)

        self.movimentando_direita = False
        self.movimentando_esquerda = False

    def update(self):
        """ ATUALIZA A POSIÇÃO DA NAVE COM FLAG """
        if self.movimentando_direita and self.local.right < self.rect.right:
            self.x += self.configuracoes.velocidade

        if self.movimentando_esquerda and self.local.left > 0:
            self.x -= self.configuracoes.velocidade

        self.local.x = self.x

    


    def desenhar_nave(self):
        self.tela.blit(self.imagem, self.local)
