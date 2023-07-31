import sys
import pygame
from configuracoes import Configuracoes
from espaconave import EspacoNave
from bala import Bala
from alienigena import Alienigena

class InvasaoAlienigena:
    """ CLASSE GERAL PARA GERENCIAR ATIVOS E COMPORTAMENTOS """
    def __init__(self):
        """ INICIALIZA O JOGO E CRIA OS RECURSOS """
        pygame.init()
        self.relogio = pygame.time.Clock()
        self.configuracoes = Configuracoes()

        self.tela = pygame.display.set_mode((self.configuracoes.largura_da_tela, self.configuracoes.altura_da_tela))
        pygame.display.set_caption("Invasão Alienigena")

        self.espaconave = EspacoNave(self)
        self.balas = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    

    def run_game(self):
        """ INICIA O LOOP PRINCIPAL """
        while True:
            #OBSERVANDO EVENTOS DE TECLADO E MOUSE
            self._checar_eventos()
            self.espaconave.update()
            self._atualizar_balas()
            self.update_aliens()
            self._atualizar_tela()          
            self.relogio.tick(60)

    def _checar_eventos(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._checar_keydown_evento(event)                        
                elif event.type == pygame.KEYUP:
                    self._checar_keyup_evento(event)
                        

    def _checar_keydown_evento(self, event):
        
        if event.key == pygame.K_RIGHT:
            self.espaconave.movimentando_direita = True
        elif event.key == pygame.K_LEFT:
            self.espaconave.movimentando_esquerda = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._atirar_bala()

    def _checar_keyup_evento(self, event):

        if event.key == pygame.K_RIGHT:
            self.espaconave.movimentando_direita = False
        if event.key == pygame.K_LEFT:
            self.espaconave.movimentando_esquerda = False

    def _atualizar_balas(self):
        self.balas.update()   

        for bala in self.balas.copy():
            if bala.rect.bottom <= 0:
                self.balar.remove(bala)

            self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.balas, self.aliens, True, True)
        if not self.aliens:
            self.balas.empty()
            self._create_fleet()

    def _atirar_bala(self):
        if len(self.balas) < self.configuracoes.bala_quantidade:
            nova_bala = Bala(self)
            self.balas.add(nova_bala)

    def _create_fleet(self):
        alien = Alienigena(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.configuracoes.altura_da_tela - 3 * alien_height):
            while current_x < (self.configuracoes.largura_da_tela - 2 * alien_width):
                self._create_alien(current_x, current_y)            
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Alienigena(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.configuracoes.fleet_drop_speed
        self.configuracoes.fleet_direction *= -1

    def update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        collided = not pygame.sprite.spritecollideany(self.espaconave, self.aliens)
        if collided:
            print(f"Alien position: {collided.rect.topleft}, Ship position: {self.espaconave.local.topleft}")
            print("Dano na Nave")

    def _atualizar_tela(self):         
         self.tela.fill(self.configuracoes.fundo_da_tela)

         for bala in self.balas.sprites():
             bala.desenhar_bala()

         self.espaconave.desenhar_nave()   
         self.aliens.draw(self.tela)

        #DEIXANDO A TELA MAIS RECENTE VISIVEL
         pygame.display.flip()



if __name__ == '__main__':
    ai = InvasaoAlienigena()
    ai.run_game()