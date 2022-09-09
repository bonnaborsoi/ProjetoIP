import pygame as pg
import time
from NovoSistemaArquitetado.Componentes.Janela.Logica import LogicaTela as LT
from NovoSistemaArquitetado.Componentes.Jogador.Logica import AtualizarJogador as AJ
from NovoSistemaArquitetado.Componentes.Inimigo.Logica import AtualizarInimigo as AI
from NovoSistemaArquitetado.Componentes.HUD.Logica import LogicaContador as LC
from NovoSistemaArquitetado.Componentes.Colecionaveis.Logica import AtualizarPokebola as AP1
from NovoSistemaArquitetado.Componentes.Colecionaveis.Logica import AtualizarPokemon as AP2
from NovoSistemaArquitetado.Componentes.Pokebola.Logica import AtualizarPokebolaArremessavel as APb

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
    from NovoSistemaArquitetado.Componentes.Sons.Logica import LogicaMusica
    AJ.AtualizarJogador()
    AI.AtualizarInimigo()
    AP1.AtualizarPokebola()
    AP2.AtualizarPokemon()
    APb.AtualizarPokebolaArremessavel()
    AtualizarJanela()
    TempoAposExecucao = time.time()
    TempoDeEspera = (1 - (TempoAposExecucao - TempoInicio)) / 180
    time.sleep(TempoDeEspera)
    TempoAposSleep = time.time()
    LC.Contador(TempoInicio,TempoAposSleep)

def TelaInicial():
    LT.CarregarTelaInicial()
    pg.display.update()

def TelaFinal():
    LT.CarregarTelaFinal()
    pg.display.update()