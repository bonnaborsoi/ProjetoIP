import pygame as pg
from NovoSistemaArquitetado.Componentes.Pokebola.Dados import DadosPokebolaArremessavel as DP1
from NovoSistemaArquitetado.Componentes.Jogador.Dados import DadosJogador as DJ
from NovoSistemaArquitetado.Componentes.HUD.Dados import DadosPokebolasColetadas as DPC

def LogicaInputsPokebola():
    teclas = pg.key.get_pressed()
    if not DP1.Arremessada:
        DP1.XPokebola, DP1.YPokebola = (DJ.XJogador//35)*35, (DJ.YJogador//35)*35
        if teclas[pg.K_e]:
            if DPC.NumeroPokebolas>0:
                if DJ.JogadorVoltadoDireita:
                    DP1.PokebolaMovendoDireita = True
                if DJ.JogadorVoltadoEsquerda:
                    DP1.PokebolaMovendoEsquerda = True
                if DJ.JogadorVoltadoAbaixo:
                    DP1.PokebolaMovendoAbaixo = True
                if DJ.JogadorVoltadoAcima:
                    DP1.PokebolaMovendoAcima = True
                DPC.NumeroPokebolas -= 1
                DPC.PokebolasColetadas = DPC.FontePokebolas.render(str(DPC.NumeroPokebolas), True, (255, 255, 255))
                DP1.Arremessada = True