import pygame as pg
from NovoSistemaArquitetado.Componentes.Pokebola.Dados import DadosPokebola1 as DP1

def SpritePokebolaDireita():
    if DP1.DireitaPokebola==20:
        DP1.DireitaPokebola = 0
    if DP1.DireitaPokebola in range (0,4):
        return(pg.image.load('Componentes/Pokebola/Recursos/PokebolaDireita1.png'))
    if DP1.DireitaPokebola in range (4,10):
        return(pg.image.load('Componentes/Pokebola/Recursos/PokebolaDireita2.png'))
    if DP1.DireitaPokebola in range (10,14):
        return(pg.image.load('Componentes/Pokebola/Recursos/PokebolaDireita3.png'))
    if DP1.DireitaPokebola in range (14,20):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaDireita4.png'))
def SpritePokebolaEsquerda():
    if DP1.EsquerdaPokebola == 20:
        DP1.EsquerdaPokebola = 0
    if DP1.EsquerdaPokebola in range(0, 4):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaEsquerda1.png'))
    if DP1.EsquerdaPokebola in range(4, 10):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaEsquerda2.png'))
    if DP1.EsquerdaPokebola in range(10, 14):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaEsquerda3.png'))
    if DP1.EsquerdaPokebola in range(14, 20):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaEsquerda4.png'))
def SpritePokebolaFrente():
    if DP1.AbaixoPokebola == 20:
        DP1.AbaixoPokebola = 0
    if DP1.AbaixoPokebola in range(0, 4):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaFrente1.png'))
    if DP1.AbaixoPokebola in range(4, 10):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaFrente2.png'))
    if DP1.AbaixoPokebola in range(10, 14):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaFrente3.png'))
    if DP1.AbaixoPokebola in range(14, 20):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaFrente4.png'))
def SpritePokebolaCostas():
    if DP1.AcimaPokebola == 20:
        DP1.AcimaPokebola = 0
    if DP1.AcimaPokebola in range(0, 4):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaCostas1.png'))
    if DP1.AcimaPokebola in range(4, 10):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaCostas2.png'))
    if DP1.AcimaPokebola in range(10, 14):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaCostas3.png'))
    if DP1.AcimaPokebola in range(14, 20):
        return (pg.image.load('Componentes/Pokebola/Recursos/PokebolaCostas4.png'))
def LogicaAnimacaoPokebola():
    if DP1.PokebolaMovendoDireita:
        DP1.DireitaPokebola += 1
        DP1.Pokebola.image = SpritePokebolaDireita()
    if DP1.PokebolaMovendoEsquerda:
        DP1.EsquerdaPokebola += 1
        DP1.Pokebola.image = SpritePokebolaEsquerda()
    if DP1.PokebolaMovendoAbaixo:
        DP1.AbaixoPokebola += 1
        DP1.Pokebola.image = SpritePokebolaFrente()
    if DP1.PokebolaMovendoAcima:
        DP1.AcimaPokebola += 1
        DP1.Pokebola.image = SpritePokebolaCostas()