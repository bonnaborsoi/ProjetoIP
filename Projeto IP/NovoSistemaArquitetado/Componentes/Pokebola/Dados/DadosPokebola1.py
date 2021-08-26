import pygame as pg

LarguraPokebola,AlturaPokebola = 35,35
XPokebola,YPokebola = 315,280
#CasaXJogador,CasaYJogador = XJogador//35,YJogador//35

#Jogador = pg.Rect(XJogador,YJogador,LarguraJogador,AlturaJogador)
GrupoPokebola = pg.sprite.Group()
Pokebola = pg.sprite.Sprite(GrupoPokebola)
Pokebola.image = pg.image.load('Componentes/Pokebola/Recursos/Pokebola.png')
#Pokebola.pngPokebola.image = pg.transform.scale(Pokebola.image, [35,35])
Pokebola.rect = pg.Rect(XPokebola,YPokebola,LarguraPokebola,AlturaPokebola)

#Situação em Relação à Animação
DireitaPokebola,EsquerdaPokebola,AcimaPokebola,AbaixoPokebola = 0,0,0,0

#Situaçaõ em Relação à Movimentação
Arremessada = False
QuantidadePassos = 0
PokebolaMovendoDireita = False
PokebolaMovendoEsquerda = False
PokebolaMovendoAbaixo = False
PokebolaMovendoAcima = False