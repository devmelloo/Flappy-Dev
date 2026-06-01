import pygame
import random

pygame.init()

tamanho = (800, 400)
pygame.display.set_caption("Flappy Dev")
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)

branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 200, 0)
azul = (90, 180, 255)
vermelho = (200, 0, 0)

fonteMenu = pygame.font.SysFont("comicsans", 25)

programador = pygame.image.load("bases/dev.png")
programador = pygame.transform.scale(programador, (80,80))


def jogar():
    posicaoXProgramador = 100
    posicaoYProgramador = 180
    larguraProgramador = 80
    alturaProgramador = 80

    movimentoYProgramador = 0
    gravidade = 1

    posicaoXErro = 800
    larguraErro = 80
    velocidadeErro = 4

    espaco = 210
    alturaErroCima = random.randint(50, 220)

    pontos = 0
    passou = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()

            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                movimentoYProgramador = -10

        movimentoYProgramador = movimentoYProgramador + gravidade
        posicaoYProgramador = posicaoYProgramador + movimentoYProgramador

        posicaoXErro = posicaoXErro - velocidadeErro

        if posicaoXErro < -larguraErro:
            posicaoXErro = 800
            alturaErroCima = random.randint(50, 220)
            passou = False

        if posicaoXErro + larguraErro < posicaoXProgramador and passou == False:
            pontos = pontos + 1
            passou = True
            velocidadeErro = velocidadeErro + 1

        tela.fill(azul)

        tela.blit(programador, (posicaoXProgramador, posicaoYProgramador))

        erroCima = pygame.draw.rect(tela, verde, (posicaoXErro, 0, larguraErro, alturaErroCima))
        erroBaixo = pygame.draw.rect(tela, verde, (posicaoXErro, alturaErroCima + espaco, larguraErro, 400))

        textoErroCima = fonteMenu.render("BUG", True, preto)
        tela.blit(textoErroCima, (posicaoXErro + 18, alturaErroCima - 35))

        textoErroBaixo = fonteMenu.render("ERROR", True, preto)
        tela.blit(textoErroBaixo, (posicaoXErro + 5, alturaErroCima + espaco + 10))

        texto = fonteMenu.render("Erros desviados: " + str(pontos), True, preto)
        tela.blit(texto, (10, 10))

        pixelsProgramadorX = list(range(posicaoXProgramador, posicaoXProgramador + larguraProgramador))
        pixelsProgramadorY = list(range(posicaoYProgramador, posicaoYProgramador + alturaProgramador))

        pixelsErroX = list(range(posicaoXErro, posicaoXErro + larguraErro))
        pixelsErroCimaY = list(range(0, alturaErroCima))
        pixelsErroBaixoY = list(range(alturaErroCima + espaco, 400))

        if len(list(set(pixelsProgramadorX).intersection(set(pixelsErroX)))) > 5:
            if len(list(set(pixelsProgramadorY).intersection(set(pixelsErroCimaY)))) > 5:
                dead(pontos)

            if len(list(set(pixelsProgramadorY).intersection(set(pixelsErroBaixoY)))) > 5:
                dead(pontos)

        if posicaoYProgramador < 0:
            dead(pontos)

        if posicaoYProgramador > 320:
            dead(pontos)

        pygame.display.update()
        relogio.tick(60)


def dead(pontos):
    larguraButtonStart = 190
    alturaButtonStart = 45

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 175
                    alturaButtonStart = 40

            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    jogar()

        tela.fill(preto)

        textoGameOver = fonteMenu.render("O bug quebrou o sistema!", True, branco)
        tela.blit(textoGameOver, (260, 120))

        textoPontos = fonteMenu.render("Erros desviados: " + str(pontos), True, branco)
        tela.blit(textoPontos, (300, 165))

        startButton = pygame.draw.rect(tela, branco, (305, 230, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Tentar novamente", True, preto)
        tela.blit(startTexto, (320, 235))

        pygame.display.update()
        relogio.tick(60)


def start():
    larguraButtonStart = 150
    alturaButtonStart = 40

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart = 35

            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    jogar()

        tela.fill(azul)

        titulo = fonteMenu.render("FLAPPY PROGRAMADOR", True, preto)
        tela.blit(titulo, (270, 110))

        instrucao = fonteMenu.render("Ajude o programador a fugir dos bugs!", True, preto)
        tela.blit(instrucao, (210, 155))

        comando = fonteMenu.render("Use a seta para cima", True, preto)
        tela.blit(comando, (295, 190))

        startButton = pygame.draw.rect(tela, branco, (325, 250, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar", True, preto)
        tela.blit(startTexto, (365, 252))

        pygame.display.update()
        relogio.tick(60)


start()