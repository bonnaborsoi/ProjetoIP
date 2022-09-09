import pygame as pg
from NovoSistemaArquitetado.Componentes.Inimigo.Logica import LogicaOrientacao as LO
from NovoSistemaArquitetado.Componentes.Inimigo.Logica import LogicaMovimentacao as LM
from NovoSistemaArquitetado.Componentes.Inimigo.Logica import LogicaAnimacao as LA
from NovoSistemaArquitetado.Componentes.Inimigo.Dados import DadosInimigo as DI

def AtualizarInimigo():
    if DI.QuantidadePassos == 14:
        DI.InimigoMovendoDireita, DI.InimigoMovendoEsquerda, DI.InimigoMovendoAbaixo, DI.InimigoMovendoAcima = False, False, False, False
        DI.Movendo = False
        DI.QuantidadePassos = 0
    LO.LogicaOrientacaoInimigo()
    LM.LogicaMovimentacaoInimigo()
    LA.LogicaAnimacaoInimigo()
    DI.Inimigo.rect = pg.Rect(DI.XInimigo, DI.YInimigo, DI.LarguraInimigo, DI.AlturaInimigo)
    DI.Inimigo.image = pg.transform.scale(DI.Inimigo.image, [36, 36])