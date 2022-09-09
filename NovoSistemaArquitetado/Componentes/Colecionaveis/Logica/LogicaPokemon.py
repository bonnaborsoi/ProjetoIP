import random
#from NovoSistemaArquitetado.Componentes.Jogador.Dados import DadosJogador as DJ
from NovoSistemaArquitetado.Componentes.Pokebola.Dados import DadosPokebolaArremessavel as DP1
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokemon as DP
from NovoSistemaArquitetado.Componentes.HUD.Dados import DadosPokemonsColetados as DPC
from NovoSistemaArquitetado.Componentes.Inimigo.Dados import DadosInimigo as DI
from NovoSistemaArquitetado.Componentes.HUD.Dados import DadosRocket as DR

def ColetarPokemon():
    if DP1.XPokebola == DP.XPokemon and DP1.YPokebola == DP.YPokemon and DP1.Arremessada:
        DPC.NumeroPokemons+=1
        DPC.PokemonsColetados = DPC.FontePokemons.render(str(DPC.NumeroPokemons), True, (255, 255, 255))
        DP.XPokemon,DP.YPokemon = random.randrange(0,666,35),random.randrange(0,596,35)
        DP1.Arremessada = False
        DP1.PokebolaMovendoDireita, DP1.PokebolaMovendoEsquerda, DP1.PokebolaMovendoAbaixo, DP1.PokebolaMovendoAcima = False, False, False, False
    if DI.XInimigo == DP.XPokemon and DI.YInimigo == DP.YPokemon:
        DR.NumeroRocket+=1
        DR.RocketColetados = DR.FonteRocket.render(str(DR.NumeroRocket), True, (255, 255, 255))
        DP.XPokemon,DP.YPokemon = random.randrange(0,666,35),random.randrange(0,596,35)
        DI.Movendo = False
        DI.InimigoMovendoDireita, DI.InimigoMovendoEsquerda, DI.InimigoMovendoAbaixo, DI.InimigoMovendoAcima = False, False, False, False