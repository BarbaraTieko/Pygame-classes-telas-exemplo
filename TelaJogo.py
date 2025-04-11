import pygame
from constantes import *

class TelaJogo:
    def __init__(self):
        # Aqui você poderia carregar os assets necessários para esta tela específica,
        # assim como inicializar os objetos que serão usados nesta tela.
        fonte_padrao = pygame.font.get_default_font()
        self.fonte_48 = pygame.font.Font(fonte_padrao, 48)
        self.fonte_20 = pygame.font.Font(fonte_padrao, 20)
        

    def desenha(self, window):
        window.fill((51,255,199))

        imagem_texto = self.fonte_48.render('TELA DE JOGO', True, (255, 51, 252))
        rect_texto = imagem_texto.get_rect()
        rect_texto.center = (WIDTH // 2, HEIGHT // 2)
        window.blit(imagem_texto, rect_texto)

        imagem_texto_2 = self.fonte_20.render('Pressione ESPAÇO para continuar', True, (255, 51, 252))
        rect_texto_2 = imagem_texto_2.get_rect()
        rect_texto_2.center = (WIDTH // 2, HEIGHT // 2 + 50)
        window.blit(imagem_texto_2, rect_texto_2)
        pygame.display.update()

    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return SAIR
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return GAME_OVER
        return JOGO