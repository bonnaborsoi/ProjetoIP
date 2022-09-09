import pygame as pg
from NovoSistemaArquitetado.Componentes.Jogador.Logica import LogicaInputs as LI
from NovoSistemaArquitetado.Componentes.Jogador.Logica import LogicaMovimentacao as LM
from NovoSistemaArquitetado.Componentes.Jogador.Logica import LogicaAnimacao as LA
from NovoSistemaArquitetado.Componentes.Jogador.Dados import DadosJogador as DJ

def AtualizarJogador():
    if DJ.QuantidadePassos == 10:
        DJ.JogadorMovendoDireita, DJ.JogadorMovendoEsquerda, DJ.JogadorMovendoAbaixo, DJ.JogadorMovendoAcima = False, False, False, False
        DJ.Movendo = False
        DJ.QuantidadePassos = 0
    LI.LogicaInputsJogador()
    LM.LogicaMovimentacaoJogador()
    LA.LogicaAnimacaoJogador()
    DJ.Jogador.rect = pg.Rect(DJ.XJogador, DJ.YJogador, DJ.LarguraJogador, DJ.AlturaJogador)