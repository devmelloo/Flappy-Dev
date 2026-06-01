import pygame
import random
from recursos.funcoes import inicializarBancoDeDados, escreverDados, maior_pontuador

pygame.init()
pygame.mixer.music.load("bases/soundtrack.mp3")

inicializarBancoDeDados()

while True:
    nome = input("Nickname: ")
    if len(nome) > 0:
        break
    else:
        print("Nome Inválido!")

tamanho = (1000, 700)
pygame.display.set_caption("Flappy Dev")
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)

branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 200, 0)
azul = (90, 180, 255)

fonteMenu = pygame.font.SysFont("comicsans", 25)

programador = pygame.image.load("bases/dev.png")
programador = pygame.transform.scale(programador, (80, 80))

decorativo = pygame.image.load("bases/bug.png")
decorativo = pygame.transform.scale(decorativo, (50, 50))

fundo = pygame.image.load("bases/fundo.png")
fundo = pygame.transform.scale(fundo, (1000, 700))


def boas_vindas():
    nome_maior, maior_pontos, dataJogada = maior_pontuador()

    larguraButtonStart = 180
    alturaButtonStart = 45

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 165
                    alturaButtonStart = 40

            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    jogar()

        tela.blit(fundo, (0,0))

        titulo = fonteMenu.render("Bem-vindo, " + nome + "!", True, preto)
        tela.blit(titulo, (370, 120))

        explicacao1 = fonteMenu.render("Ajude o programador a fugir dos bugs e erros.", True, preto)
        tela.blit(explicacao1, (260, 180))

        explicacao2 = fonteMenu.render("Use a seta para cima para voar.", True, preto)
        tela.blit(explicacao2, (330, 220))

        if nome_maior == None:
            recorde = fonteMenu.render("Melhor jogador: ainda nao existe", True, preto)
            tela.blit(recorde, (330, 290))
        else:
            recorde = fonteMenu.render("Melhor jogador: " + nome_maior + " - " + str(maior_pontos), True, preto)
            tela.blit(recorde, (310, 290))

            data = fonteMenu.render("Data/Hora: " + str(dataJogada), True, preto)
            tela.blit(data, (370, 325))

        startButton = pygame.draw.rect(tela, branco, (400, 430, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar partida", True, preto)
        tela.blit(startTexto, (415, 435))

        pygame.display.update()
        relogio.tick(60)


def jogar():
    pygame.mixer.music.play(-1)

    posicaoXProgramador = 100
    posicaoYProgramador = 300
    larguraProgramador = 80
    alturaProgramador = 80

    posicaoXDecorativo = random.randint(100, 900)
    posicaoYDecorativo = random.randint(50, 600)

    movimentoXDecorativo = random.randint(-3, 3)
    movimentoYDecorativo = random.randint(-3, 3)


    movimentoYProgramador = 0
    gravidade = 1

    posicaoXErro = 1000
    larguraErro = 80
    velocidadeErro = 3

    espaco = 240
    alturaErroCima = random.randint(80, 320)

    pontos = 0
    passou = False
    pausado = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()

            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                movimentoYProgramador = -13

            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                pausado = not pausado

        posicaoXDecorativo = posicaoXDecorativo + movimentoXDecorativo
        posicaoYDecorativo = posicaoYDecorativo + movimentoYDecorativo

        if posicaoXDecorativo <= 0:
            movimentoXDecorativo = random.randint(1, 4)

        elif posicaoXDecorativo >= 950:
            movimentoXDecorativo = random.randint(-4, -1)

        if posicaoYDecorativo <= 0:
            movimentoYDecorativo = random.randint(1, 4)

        elif posicaoYDecorativo >= 650:
            movimentoYDecorativo = random.randint(-4, -1)
        
        if random.randint(1, 100) == 1:
            movimentoXDecorativo = random.randint(-3, 3)
            movimentoYDecorativo = random.randint(-3, 3)

        if pausado == True:
            textoPausa = fonteMenu.render("PAUSADO - Aperte SPACE para continuar", True, branco)
            tela.blit(textoPausa, (300, 330))
            pygame.display.update()
            relogio.tick(60)
            continue

        movimentoYProgramador = movimentoYProgramador + gravidade
        posicaoYProgramador = posicaoYProgramador + movimentoYProgramador

        posicaoXErro = posicaoXErro - velocidadeErro

        if posicaoXErro < -larguraErro:
            posicaoXErro = 1000
            alturaErroCima = random.randint(80, 320)
            passou = False

        if posicaoXErro + larguraErro < posicaoXProgramador and passou == False:
            pontos = pontos + 1
            passou = True

            if pontos % 3 == 0:
                velocidadeErro = velocidadeErro + 1

        tela.blit(fundo, (0,0))
        tela.blit(decorativo, (posicaoXDecorativo, posicaoYDecorativo))
        tela.blit(programador, (posicaoXProgramador, posicaoYProgramador))

        pygame.draw.rect(tela, verde, (posicaoXErro, 0, larguraErro, alturaErroCima))
        pygame.draw.rect(tela, verde, (posicaoXErro, alturaErroCima + espaco, larguraErro, 700))

        textoErroCima = fonteMenu.render("BUG", True, preto)
        tela.blit(textoErroCima, (posicaoXErro + 18, alturaErroCima - 35))

        textoErroBaixo = fonteMenu.render("ERROR", True, preto)
        tela.blit(textoErroBaixo, (posicaoXErro + 5, alturaErroCima + espaco + 10))

        texto = fonteMenu.render("Erros desviados: " + str(pontos), True, branco)
        tela.blit(texto, (10, 10))

        textoPause = fonteMenu.render("SPACE = Pause", True, branco)
        tela.blit(textoPause, (820, 10))

        pixelsProgramadorX = list(range(posicaoXProgramador, posicaoXProgramador + larguraProgramador))
        pixelsProgramadorY = list(range(posicaoYProgramador, posicaoYProgramador + alturaProgramador))

        pixelsErroX = list(range(posicaoXErro, posicaoXErro + larguraErro))
        pixelsErroCimaY = list(range(0, alturaErroCima))
        pixelsErroBaixoY = list(range(alturaErroCima + espaco, 700))

        if len(list(set(pixelsProgramadorX).intersection(set(pixelsErroX)))) > 5:
            if len(list(set(pixelsProgramadorY).intersection(set(pixelsErroCimaY)))) > 5:
                escreverDados(nome, pontos)
                dead(pontos)

            if len(list(set(pixelsProgramadorY).intersection(set(pixelsErroBaixoY)))) > 5:
                escreverDados(nome, pontos)
                dead(pontos)

        if posicaoYProgramador < 0:
            escreverDados(nome, pontos)
            dead(pontos)

        if posicaoYProgramador > 620:
            escreverDados(nome, pontos)
            dead(pontos)

        pygame.display.update()
        relogio.tick(60)


def dead(pontos):
    pygame.mixer.music.stop()

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
                    boas_vindas()

        tela.fill(preto)

        textoGameOver = fonteMenu.render("O bug quebrou o sistema!", True, branco)
        tela.blit(textoGameOver, (340, 180))

        textoPontos = fonteMenu.render("Erros desviados: " + str(pontos), True, branco)
        tela.blit(textoPontos, (380, 230))

        startButton = pygame.draw.rect(tela, branco, (390, 320, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Tentar novamente", True, preto)
        tela.blit(startTexto, (405, 325))

        pygame.display.update()
        relogio.tick(60)


boas_vindas()