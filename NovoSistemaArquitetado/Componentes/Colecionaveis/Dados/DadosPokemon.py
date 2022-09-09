import pygame as pg
import random

LarguraPokemon,AlturaPokemon = 35,35
XPokemon,YPokemon = random.randrange(0,666,35),random.randrange(0,596,35)

GrupoPokemon = pg.sprite.Group()
Pokemon = pg.sprite.Sprite(GrupoPokemon)
Pokemon.image = pg.image.load('Componentes/Colecionaveis/Recursos/Pikachu.png')
Pokemon.image = pg.transform.scale(Pokemon.image, [50,50])
Pokemon.rect = pg.Rect(XPokemon,YPokemon,LarguraPokemon,AlturaPokemon)