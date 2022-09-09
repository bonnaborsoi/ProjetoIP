import pygame as pg
pg.init()

Fonte = pg.font.SysFont('Consolas', 30)
TempoCorrido, TempoRestante, Texto = 0, 60, '60'.rjust(3)
TempoParaContador = 0
MenorQue10 = False