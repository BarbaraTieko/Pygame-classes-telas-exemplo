import pygame
from constantes import *
from TelaInicio import TelaInicio
from TelaJogo import TelaJogo   
from TelaGameOver import TelaGameOver

class Jogo:
    def __init__(self):
        pygame.init()
        self.largura_janela = WIDTH
        self.altura_janela = HEIGHT
        self.window = pygame.display.set_mode((self.largura_janela, self.altura_janela))

        # Não precisamos mais de um dicionário para guardar o estado.
        # Podemos armazenar os dados diretamente como atributos.
        self.tela_atual_chave = INICIO
        self.telas = {
            INICIO: TelaInicio(),
            JOGO: TelaJogo(),
            GAME_OVER: TelaGameOver()
        }

    def roda(self):
        # Este método ficou um pouco mais complexo do que antes, mas agora podemos ter 
        # quantas e quais telas quisermos, sem precisar nos preocupar com o que deve acontecer
        # em cada uma delas.
        

        
        while self.tela_atual_chave != SAIR:

            tela_atual = self.telas[self.tela_atual_chave]
            self.tela_atual_chave = tela_atual.atualiza()
            tela_atual.desenha(self.window)


if __name__ == '__main__':
    Jogo().roda()