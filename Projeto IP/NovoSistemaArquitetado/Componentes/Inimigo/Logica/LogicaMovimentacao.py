from NovoSistemaArquitetado.Componentes.Inimigo.Dados import DadosInimigo as DI

def LogicaMovimentacaoInimigo():
    if DI.InimigoMovendoDireita:
        DI.QuantidadePassos += 1
        DI.XInimigo += 2.5
    if DI.InimigoMovendoEsquerda:
        DI.QuantidadePassos += 1
        DI.XInimigo -= 2.5
    if DI.InimigoMovendoAbaixo:
        DI.QuantidadePassos += 1
        DI.YInimigo += 2.5
    if DI.InimigoMovendoAcima:
        DI.QuantidadePassos += 1
        DI.YInimigo -= 2.5