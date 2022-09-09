import pygame as pg
from NovoSistemaArquitetado.Componentes.Janela.Dados import DadosJanela as DT
from NovoSistemaArquitetado.Componentes.Janela.Dados import DadosTelaInicial as DTI
from NovoSistemaArquitetado.Componentes.Mapa.Dados import DadosMapa as DM
from NovoSistemaArquitetado.Componentes.Jogador.Dados import DadosJogador as DJ
from NovoSistemaArquitetado.Componentes.Inimigo.Dados import DadosInimigo as DI
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola as DP1
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola2 as DP2
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola3 as DP3
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola4 as DP4
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola5 as DP5
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokemon as DPk
from NovoSistemaArquitetado.Componentes.HUD.Dados import DadosPokebolasColetadas as DPC1
from NovoSistemaArquitetado.Componentes.HUD.Dados import DadosPokemonsColetados as DPC2
from NovoSistemaArquitetado.Componentes.HUD.Dados import DadosRocket as DR
from NovoSistemaArquitetado.Componentes.HUD.Dados import DadosContador as DC
from NovoSistemaArquitetado.Componentes.Pokebola.Dados import DadosPokebolaArremessavel as DPb
from NovoSistemaArquitetado.Componentes.Janela.Dados import DadosTelaFinal as DTF

#Criar a janela (fora do loop)
Janela = pg.display.set_mode([DT.LarguraJanela,DT.AlturaJanela])
#Nome e Icone do Jogo
pg.display.set_caption("Gotta catch 'em all")
pg.display.set_icon(DT.Icone)

def CarregarTelaInicial():
    Janela.fill((0, 0, 0))
    Janela.blit(DTI.TelaInicial, (0, 0))
def CarregarTelaFinal():
    if DTF.Sucesso:
        Janela.blit(DTF.Fonte.render(DTF.TextoSucesso, True, (255, 255, 255)), (200, 320))
    if DTF.Derrota:
        Janela.blit(DTF.Fonte.render(DTF.TextoDerrota, True, (255, 255, 255)), (170, 320))
def CarregarMapa():
    Janela.fill((0, 0, 0))
    Janela.blit(DM.Mapa, (0, 0))
def CarregarJogador():
    DJ.GrupoJogador.draw(Janela)
def CarregarInimigo():
    DI.GrupoInimigo.draw(Janela)
def CarregarPokebolaColecionavel():
    DP1.GrupoPokebola.draw(Janela)
    DP2.GrupoPokebola.draw(Janela)
    DP3.GrupoPokebola.draw(Janela)
    DP4.GrupoPokebola.draw(Janela)
    DP5.GrupoPokebola.draw(Janela)
def CarregarPokemonColecionavel():
    DPk.GrupoPokemon.draw(Janela)
def CarregarPokebolaArremessavel():
    if DPb.Arremessada:
        DPb.GrupoPokebola.draw(Janela)
def CarregarHUD():
    Janela.blit(DPC1.PokebolasColetadas, (50, 15))
    Janela.blit(DPC1.IconePokebola, (10, 10))
    Janela.blit(DPC2.PokemonsColetados, (50, 50))
    Janela.blit(DPC2.IconePokemon, (10, 45))
    Janela.blit(DR.RocketColetados, (50,85))
    Janela.blit(DR.IconeRocket, (10,80))
    if not DC.MenorQue10:
        Janela.blit(DC.Fonte.render(DC.Texto, True, (255, 255, 255)), (655, 10))
    else:
        Janela.blit(DC.Fonte.render(DC.Texto, True, (255, 255, 255)), (673, 10))
