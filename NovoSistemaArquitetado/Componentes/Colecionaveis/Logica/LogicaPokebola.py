import random
from NovoSistemaArquitetado.Componentes.Jogador.Dados import DadosJogador as DJ
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola as DP
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola2 as DP2
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola3 as DP3
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola4 as DP4
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokebola5 as DP5
from NovoSistemaArquitetado.Componentes.HUD.Dados import DadosPokebolasColetadas as DPC

def ColetarPokebola():
    if DJ.XJogador == DP.XPokebola and DJ.YJogador == DP.YPokebola:
        DPC.NumeroPokebolas+=1
        DPC.PokebolasColetadas = DPC.FontePokebolas.render(str(DPC.NumeroPokebolas), True, (255, 255, 255))
        DP.XPokebola,DP.YPokebola = random.randrange(0,666,35),random.randrange(0,596,35)
    if DJ.XJogador == DP2.XPokebola and DJ.YJogador == DP2.YPokebola:
        DPC.NumeroPokebolas+=1
        DPC.PokebolasColetadas = DPC.FontePokebolas.render(str(DPC.NumeroPokebolas), True, (255, 255, 255))
        DP2.XPokebola,DP2.YPokebola = random.randrange(0,666,35),random.randrange(0,596,35)
    if DJ.XJogador == DP3.XPokebola and DJ.YJogador == DP3.YPokebola:
        DPC.NumeroPokebolas+=1
        DPC.PokebolasColetadas = DPC.FontePokebolas.render(str(DPC.NumeroPokebolas), True, (255, 255, 255))
        DP3.XPokebola,DP3.YPokebola = random.randrange(0,666,35),random.randrange(0,596,35)
    if DJ.XJogador == DP4.XPokebola and DJ.YJogador == DP4.YPokebola:
        DPC.NumeroPokebolas+=1
        DPC.PokebolasColetadas = DPC.FontePokebolas.render(str(DPC.NumeroPokebolas), True, (255, 255, 255))
        DP4.XPokebola,DP4.YPokebola = random.randrange(0,666,35),random.randrange(0,596,35)
    if DJ.XJogador == DP5.XPokebola and DJ.YJogador == DP5.YPokebola:
        DPC.NumeroPokebolas+=1
        DPC.PokebolasColetadas = DPC.FontePokebolas.render(str(DPC.NumeroPokebolas), True, (255, 255, 255))
        DP5.XPokebola,DP5.YPokebola = random.randrange(0,666,35),random.randrange(0,596,35)