import pygame as pg
import random

#Exibicao do Inimigo
LarguraInimigo,AlturaInimigo = 35,35
XInimigo,YInimigo = random.randrange(0,666,35),random.randrange(0,596,35)
CasaXInimigo,CasaYInimigo = XInimigo//35,YInimigo//35

GrupoInimigo = pg.sprite.Group()
Inimigo = pg.sprite.Sprite(GrupoInimigo)
Inimigo.image = pg.image.load('Componentes/Inimigo/Recursos/InimigoFrente1.png')
Inimigo.image = pg.transform.scale(Inimigo.image, [36,36])
Inimigo.rect = pg.Rect(XInimigo,YInimigo,LarguraInimigo,AlturaInimigo)

#Situação em Relação à Animaçaõ
Movendo = False
DireitaInimigo,EsquerdaInimigo,AcimaInimigo,AbaixoInimigo = 0,0,0,0
QuantidadePassos = 0
InimigoMovendo = False
InimigoMovendoDireita = False
InimigoMovendoEsquerda = False
InimigoMovendoAbaixo = False
InimigoMovendoAcima = False