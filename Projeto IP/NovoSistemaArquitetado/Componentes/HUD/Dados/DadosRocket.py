import pygame as pg
pg.init()

# --> INICIALIZAÇÃO DA TELA /NOME DA JANELA(GAME)/ CARREGAR A IMAGEM DO map/ SETAR O ICONE DO JOGO NA ABA
IconeRocket = pg.image.load("Componentes/HUD/Recursos/Coletados/Rocket.png")
IconeRocket = pg.transform.smoothscale(IconeRocket, (30, 30))

# --> PONTUAÇÃO DO JOGO
NumeroRocket = 0
FonteRocket = pg.font.Font("freesansbold.ttf", 25)
RocketColetados = FonteRocket.render(str(NumeroRocket), True, (255, 255, 255))