import pygame as pg
import random

#Exibicao do Jogador
LarguraJogador,AlturaJogador = 35,35
XJogador,YJogador = random.randrange(0,666,35),random.randrange(0,596,35)

#Jogador = pg.Rect(XJogador,YJogador,LarguraJogador,AlturaJogador)
GrupoJogador = pg.sprite.Group()
Jogador = pg.sprite.Sprite(GrupoJogador)
Jogador.image = pg.image.load('Componentes/Jogador/Recursos/Jogador_FrenteB.png')
Jogador.image = pg.transform.scale(Jogador.image, [35,35])
Jogador.rect = pg.Rect(XJogador,YJogador,LarguraJogador,AlturaJogador)

#Situação em Relação à Animação
DireitaJogador,EsquerdaJogador,AcimaJogador,AbaixoJogador = 0,0,0,0

#Situação Quanto à Direção do Jogador
JogadorVoltadoDireita = False
JogadorVoltadoEsquerda = False
JogadorVoltadoAbaixo = True
JogadorVoltadoAcima = False

#Situaçaõ em Relação à Movimentação
QuantidadePassos = 0
JogadorMovendoDireita = False
JogadorMovendoEsquerda = False
JogadorMovendoAbaixo = False
JogadorMovendoAcima = False