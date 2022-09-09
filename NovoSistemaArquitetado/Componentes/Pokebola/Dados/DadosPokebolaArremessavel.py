import pygame as pg

LarguraPokebola,AlturaPokebola = 35,35
XPokebola,YPokebola = 315,280

GrupoPokebola = pg.sprite.Group()
Pokebola = pg.sprite.Sprite(GrupoPokebola)
Pokebola.image = pg.image.load('Componentes/Pokebola/Recursos/PokebolaFrente1.png')
Pokebola.rect = pg.Rect(XPokebola,YPokebola,LarguraPokebola,AlturaPokebola)

#Situação em Relação à Animação
DireitaPokebola,EsquerdaPokebola,AcimaPokebola,AbaixoPokebola = 0,0,0,0

#Situaçaõ em Relação à Movimentação
Arremessada = False
PokebolaMovendoDireita = False
PokebolaMovendoEsquerda = False
PokebolaMovendoAbaixo = False
PokebolaMovendoAcima = False