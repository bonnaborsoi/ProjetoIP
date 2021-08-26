import pygame as pg
import random

LarguraPokebola,AlturaPokebola = 35,35
XPokebola,YPokebola = random.randrange(0,666,35),random.randrange(0,596,35)
CasaXPokebola,CasaYPokebola = XPokebola//35,YPokebola//35

GrupoPokebola = pg.sprite.Group()
Pokebola = pg.sprite.Sprite(GrupoPokebola)
Pokebola.image = pg.image.load('Componentes/Colecionaveis/Recursos/Pokebola.png')
Pokebola.image = pg.transform.scale(Pokebola.image, [35,35])
Pokebola.rect = pg.Rect(XPokebola,YPokebola,LarguraPokebola,AlturaPokebola)