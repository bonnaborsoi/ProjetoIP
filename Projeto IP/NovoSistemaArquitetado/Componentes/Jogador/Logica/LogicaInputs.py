import pygame as pg
from NovoSistemaArquitetado.Componentes.Janela.Dados import DadosJanela as DT
from NovoSistemaArquitetado.Componentes.Jogador.Dados import DadosJogador as DJ

def LogicaInputsJogador():
    teclas = pg.key.get_pressed()
    if teclas[pg.K_d] and DJ.XJogador < DT.LarguraJanela - DJ.LarguraJogador:
        if  not DJ.JogadorMovendoEsquerda and not DJ.JogadorMovendoAbaixo and not DJ.JogadorMovendoAcima:
            DJ.JogadorVoltadoDireita = True
            DJ.JogadorVoltadoEsquerda = False
            DJ.JogadorVoltadoAbaixo = False
            DJ.JogadorVoltadoAcima = False
            DJ.JogadorMovendoDireita = True
    if teclas[pg.K_a] and DJ.XJogador > 0:
        if  not DJ.JogadorMovendoDireita and not DJ.JogadorMovendoAbaixo and not DJ.JogadorMovendoAcima:
            DJ.JogadorVoltadoEsquerda = True
            DJ.JogadorVoltadoDireita = False
            DJ.JogadorVoltadoAbaixo = False
            DJ.JogadorVoltadoAcima = False
            DJ.JogadorMovendoEsquerda = True
    if teclas[pg.K_s] and DJ.YJogador < DT.AlturaJanela - DJ.LarguraJogador:
        if  not DJ.JogadorMovendoDireita and not DJ.JogadorMovendoEsquerda and not DJ.JogadorMovendoAcima:
            DJ.JogadorVoltadoAbaixo = True
            DJ.JogadorVoltadoDireita = False
            DJ.JogadorVoltadoEsquerda = False
            DJ.JogadorVoltadoAcima = False
            DJ.JogadorMovendoAbaixo = True
    if teclas[pg.K_w] and DJ.YJogador > 0:
        if  not DJ.JogadorMovendoDireita and not DJ.JogadorMovendoEsquerda and not DJ.JogadorMovendoAbaixo:
            DJ.JogadorVoltadoAcima = True
            DJ.JogadorVoltadoDireita = False
            DJ.JogadorVoltadoEsquerda = False
            DJ.JogadorVoltadoAbaixo = False
            DJ.JogadorMovendoAcima = True