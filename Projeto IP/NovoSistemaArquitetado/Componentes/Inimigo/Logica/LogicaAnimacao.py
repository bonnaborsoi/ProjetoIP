import pygame as pg
from NovoSistemaArquitetado.Componentes.Inimigo.Dados import DadosInimigo as DI

def SpriteInimigoDireita():
    if DI.DireitaInimigo==28:
        DI.DireitaInimigo = 0
    if DI.DireitaInimigo in range (0,6):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoDireita1.png'))
    if DI.DireitaInimigo in range (6,14):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoDireita2.png'))
    if DI.DireitaInimigo in range (14,20):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoDireita1.png'))
    if DI.DireitaInimigo in range (20,28):
        return (pg.image.load('Componentes/Inimigo/Recursos/InimigoDireita3.png'))
def SpriteInimigoEsquerda():
    if DI.EsquerdaInimigo==28:
        DI.EsquerdaInimigo = 0
    if DI.EsquerdaInimigo in range (0,6):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoEsquerda1.png'))
    if DI.EsquerdaInimigo in range (6,14):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoEsquerda2.png'))
    if DI.EsquerdaInimigo in range (14,20):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoEsquerda1.png'))
    if DI.EsquerdaInimigo in range (20,28):
        return (pg.image.load('Componentes/Inimigo/Recursos/InimigoEsquerda3.png'))
def SpriteInimigoFrente():
    if DI.AbaixoInimigo==28:
        DI.AbaixoInimigo = 0
    if DI.AbaixoInimigo in range (0,6):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoFrente1.png'))
    if DI.AbaixoInimigo in range (6,14):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoFrente2.png'))
    if DI.AbaixoInimigo in range (14,20):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoFrente1.png'))
    if DI.AbaixoInimigo in range (20,28):
        return (pg.image.load('Componentes/Inimigo/Recursos/InimigoFrente3.png'))
def SpriteInimigoCostas():
    if DI.AcimaInimigo==28:
        DI.AcimaInimigo = 0
    if DI.AcimaInimigo in range (0,6):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoCostas1.png'))
    if DI.AcimaInimigo in range (6,14):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoCostas2.png'))
    if DI.AcimaInimigo in range (14,20):
        return(pg.image.load('Componentes/Inimigo/Recursos/InimigoCostas1.png'))
    if DI.AcimaInimigo in range (20,28):
        return (pg.image.load('Componentes/Inimigo/Recursos/InimigoCostas3.png'))
def LogicaAnimacaoInimigo():
    if DI.InimigoMovendoDireita:
        DI.DireitaInimigo += 1
        DI.Inimigo.image = SpriteInimigoDireita()
    if DI.InimigoMovendoEsquerda:
        DI.EsquerdaInimigo += 1
        DI.Inimigo.image = SpriteInimigoEsquerda()
    if DI.InimigoMovendoAbaixo:
        DI.AbaixoInimigo += 1
        DI.Inimigo.image = SpriteInimigoFrente()
    if DI.InimigoMovendoAcima:
        DI.AcimaInimigo += 1
        DI.Inimigo.image = SpriteInimigoCostas()