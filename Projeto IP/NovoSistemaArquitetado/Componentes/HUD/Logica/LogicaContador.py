from NovoSistemaArquitetado.Componentes.HUD.Dados import DadosContador as DC
#from NovoSistemaArquitetado import RodarJogo as RJ
from NovoSistemaArquitetado.Componentes.Janela.Dados import DadosJanela as DJ

def Contador(TempoInicio,TempoAposExecucao):
    DC.TempoCorrido += TempoAposExecucao-TempoInicio
    DC.TempoParaContador += TempoAposExecucao-TempoInicio
    if DC.TempoParaContador>=1:
        DC.TempoRestante-=1
        DC.TempoParaContador-=1
    DC.Texto = str(DC.TempoRestante)
    if DC.TempoRestante<10:
        DC.MenorQue10 = True
    if DC.TempoRestante <=0:
        DJ.JanelaAberta = False
        #RJ.FecharJogo()