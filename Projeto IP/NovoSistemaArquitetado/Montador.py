import pygame as pg
import time
from NovoSistemaArquitetado.Componentes.Janela.Logica import LogicaTela as LT
from NovoSistemaArquitetado.Componentes.Janela.Dados import DadosTelaInicial as DTI
from NovoSistemaArquitetado.Componentes.Jogador.Logica import AtualizarJogador as AJ
from NovoSistemaArquitetado.Componentes.Inimigo.Logica import AtualizarInimigo as AI
from NovoSistemaArquitetado.Componentes.HUD.Logica import LogicaContador as LC
from NovoSistemaArquitetado.Componentes.Colecionaveis.Logica import AtualizarPokebola as AP1
from NovoSistemaArquitetado.Componentes.Colecionaveis.Logica import AtualizarPokemon as AP2
from NovoSistemaArquitetado.Componentes.Pokebola.Logica import AtualizarPokebolas as APb

def TocarMusicaFundo():
    from NovoSistemaArquitetado.Componentes.Sons.Logica import LogicaMusica

def AtualizarJanela():
    LT.CarregarMapa()
    LT.CarregarPokebolaColecionavel()
    LT.CarregarPokemonColecionavel()
    LT.CarregarInimigo()
    LT.CarregarJogador()
    LT.CarregarPokebolaArremessavel()
    LT.CarregarHUD()
    pg.display.update()

def Montar():
    TempoInicio = time.time()
    #TocarMusicaFundo()
    from NovoSistemaArquitetado.Componentes.Sons.Logica import LogicaMusica
    AJ.AtualizarJogador()
    AI.AtualizarInimigo()
    AP1.AtualizarPokebola()
    AP2.AtualizarPokemon()
    APb.AtualizarPokebola()
    AtualizarJanela()
    TempoAposExecucao = time.time()
    TempoDeEspera = (1 - (TempoAposExecucao - TempoInicio)) / 180
    time.sleep(TempoDeEspera)
    TempoAposSleep = time.time()
    LC.Contador(TempoInicio,TempoAposSleep)

def TelaInicial():
    #TempoInicio = time.time()
    LT.CarregarTelaInicial()
    '''Texto = True
    while Texto:
        DTI.TelaInicial = pg.image.load("Componentes/Janela/Recursos/TitleScreen2.png")
        pg.display.update()
        TempoDois = time.time()
        if TempoDois-TempoInicio >= 3:
            Texto = False'''
    #DTI.TelaInicial = pg.image.load("Componentes/Janela/Recursos/TitleScreen1.png")
    pg.display.update()

def TelaFinal():
    exit