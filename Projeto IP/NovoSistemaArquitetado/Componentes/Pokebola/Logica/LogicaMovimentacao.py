import pygame as pg
from NovoSistemaArquitetado.Componentes.Pokebola.Dados import DadosPokebola1 as DP1

def LogicaMovimentacaoPokebola():
    if DP1.PokebolaMovendoDireita:
        DP1.XPokebola += 7
    if DP1.PokebolaMovendoEsquerda:
        DP1.XPokebola -= 7
    if DP1.PokebolaMovendoAbaixo:
        DP1.QuantidadePassos += 1
        DP1.YPokebola += 7
    if DP1.PokebolaMovendoAcima:
        DP1.YPokebola -= 7