import pygame as pg
pg.init()

from NovoSistemaArquitetado.Componentes.Janela.Dados import DadosJanela as DT
from NovoSistemaArquitetado import Montador as M

StartGame = False

def RodarJogo():
    global StartGame
    # Loop do Jogo
    while DT.JanelaAberta:
        for evento in pg.event.get():
            #Para fechar a janela ao clicar no x
            if evento.type == pg.QUIT:
                DT.JanelaAberta = False
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_SPACE and not StartGame:
                    StartGame = True
        if not StartGame:
            M.TelaInicial()
        if StartGame:
            M.Montar()