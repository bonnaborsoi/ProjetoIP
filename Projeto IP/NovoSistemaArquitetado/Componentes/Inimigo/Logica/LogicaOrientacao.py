from NovoSistemaArquitetado.Componentes.Inimigo.Dados import DadosInimigo as DI
from NovoSistemaArquitetado.Componentes.Colecionaveis.Dados import DadosPokemon as DP

def LogicaOrientacaoInimigo():
    VetorX = DP.XPokemon - DI.XInimigo
    VetorY = DP.YPokemon - DI.YInimigo
    CasasX = VetorX//35
    CasasY = VetorY//35
    if not DI.Movendo:
        if VetorX>0:
            DI.InimigoMovendoDireita = True
        elif VetorX<0:
            DI.InimigoMovendoEsquerda = True
        elif VetorY>0:
            DI.InimigoMovendoAbaixo = True
        elif VetorY<0:
            DI.InimigoMovendoAcima = True
        DI.Movendo = True








    '''
    if CasasX > CasasY:
        Proporcao = CasasX//CasasY
    elif CasasY > CasasX:
        Proporcao = CasasY//CasasX
    else:
        Proporcao = 1
    if CasasX != 0:
        .
    if CasasY != 0:
    .
    if DI.CasaXInimigo > DJ.CasaXJogador:
        DI.InimigoMovendoEsquerda = True
    elif DI.CasaXInimigo < DJ.CasaXJogador:
        DI.InimigoMovendoDireita =True
    if DI.CasaYInimigo > DJ.CasaYJogador:
        DI.InimigoMovendoAbaixo = True
    elif DI.CasaYInimigo < DJ.CasaYJogador:
        DI.InimigoMovendoAcima = True
    else:
        DI.InimigoMovendoDireita, DI.InimigoMovendoEsquerda, DI.InimigoMovendoAbaixo, DI.InimigoMovendoAcima = False, False, False, False
    if DI.InimigoMovendoEsquerda and DI.QuantidadePassos<10:
        DI.QuantidadePassos +=1
        DI.XInimigo -= 1.75
    elif DI.InimigoMovendoDireita and DI.QuantidadePassos<10:
        DI.QuantidadePassos += 1
        DI.XInimigo += 1.75
    elif DI.InimigoMovendoAbaixo and DI.QuantidadePassos<10:
        DI.QuantidadePassos += 1
        DI.YInimigo -= 1.75
    elif DI.InimigoMovendoAcima > 0 and DI.QuantidadePassos<10:
        DI.QuantidadePassos += 1
        DI.YInimigo += 1.75
    '''