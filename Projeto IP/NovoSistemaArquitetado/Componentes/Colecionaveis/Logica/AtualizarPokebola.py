import pygame as pg
from NovoSistemaArquitetado.Componentes.Colecionaveis.Logica import LogicaPokebola as LP
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola as DP
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola2 as DP2
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola3 as DP3
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola4 as DP4
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola5 as DP5
def AtualizarPokebola():
    LP.ColetarPokebola()
    DP.Pokebola.rect = pg.Rect(DP.XPokebola,DP.YPokebola,DP.LarguraPokebola,DP.AlturaPokebola)
    DP2.Pokebola.rect = pg.Rect(DP2.XPokebola, DP2.YPokebola, DP2.LarguraPokebola, DP2.AlturaPokebola)
    DP3.Pokebola.rect = pg.Rect(DP3.XPokebola, DP3.YPokebola, DP3.LarguraPokebola, DP3.AlturaPokebola)
    DP4.Pokebola.rect = pg.Rect(DP4.XPokebola, DP4.YPokebola, DP4.LarguraPokebola, DP4.AlturaPokebola)
    DP5.Pokebola.rect = pg.Rect(DP5.XPokebola, DP5.YPokebola, DP5.LarguraPokebola, DP5.AlturaPokebola)