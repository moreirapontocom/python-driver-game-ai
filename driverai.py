import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 500

IMAGEM_BACKGROUND = (pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGEM_PISTA = pygame.transform.scale_by(pygame.image.load(os.path.join('imgs', 'pista.png')), 3)
IMAGEM_OBSTACULO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'obstaculo.png')))
IMAGEM_CARRO_FRENTE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'carro_frente.png')))
IMAGEM_CARRO_VIRANDO_ESQUERDA = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'carro_virando.png')))
IMAGEM_CARRO_VIRANDO_DIREITA = pygame.transform.flip(IMAGEM_CARRO_VIRANDO_ESQUERDA, True, False)

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 30)

class Carro:
    CARRO = IMAGEM_CARRO_FRENTE
    x = 200

    def __init__(self):
        pass

    def virar_carro(self, direcao):
        if direcao == 'esquerda':
            print("Esquerda")
            self.CARRO = IMAGEM_CARRO_VIRANDO_ESQUERDA
            self.x = 120
        if direcao == 'direita':
            print("Direita")
            self.CARRO = IMAGEM_CARRO_VIRANDO_DIREITA
            self.x = 250
        if direcao == 'frente':
            print("Frente")
            self.CARRO = IMAGEM_CARRO_FRENTE
            self.x = 200

    def desenhar(self, tela):
        tela.blit(self.CARRO, (self.x, 300))

class Pista:
    VELOCIDADE = 10
    ALTURA_PISTA = 350

    def __init__(self, y):
        self.y1 = y
        self.y2 = self.y1 + self.ALTURA_PISTA

    def mover(self):
        self.y1 += self.VELOCIDADE
        self.y2 += self.VELOCIDADE

        if self.y1 > TELA_ALTURA:
            print(f"y1: {self.y1}")
            self.y1 = -self.ALTURA_PISTA

        if self.y2 > TELA_ALTURA:
            self.y2 = -self.ALTURA_PISTA

    def desenhar(self, tela):
        tela.blit(IMAGEM_PISTA, (230, self.y1))
        tela.blit(IMAGEM_PISTA, (230, self.y2))
        self.mover()

class Obstaculo:
    pos_x1 = 0
    pos_y1 = 0
    pos_x2 = 0
    pos_y2 = 0
    ALTURA_OBSTACULO = 40
    VELOCIDADE = 14

    def __init__(self):
        self.pos_x1 = random.randrange(115, 290)
        self.pos_y1 = -self.ALTURA_OBSTACULO

    def mover(self):
        self.pos_y1 += self.VELOCIDADE

        if (self.pos_y1 > TELA_ALTURA + 10):
            self.pos_y1 = -self.ALTURA_OBSTACULO
            self.pos_x1 = random.randrange(115, 290)

    def desenhar(self, tela):
        tela.blit(IMAGEM_OBSTACULO, (self.pos_x1, self.pos_y1))
        self.mover()

def desenhar_tela(tela, pista, carro, obstaculo, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))

    pista.desenhar(tela)
    obstaculo.desenhar(tela)
    carro.desenhar(tela)

    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", True, (0, 0, 0))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))

    pygame.display.update()

def main():
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pista = Pista(20)
    carro = Carro()
    obstaculo = Obstaculo()

    relogio = pygame.time.Clock()
    pontos = 0

    rodando = True
    while rodando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    print("Esquerda")
                    carro.virar_carro('esquerda')
                if evento.key == pygame.K_RIGHT:
                    print("Direita")
                    carro.virar_carro('direita')
                    print("Direita")
                if evento.key == pygame.K_UP:
                    carro.virar_carro('frente')

                    pontos += 1

        desenhar_tela(tela, pista, carro, obstaculo, pontos)

if __name__ == '__main__':
    main()