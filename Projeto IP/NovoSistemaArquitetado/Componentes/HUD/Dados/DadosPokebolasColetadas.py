import pygame as pg
pg.init()

# --> INICIALIZAÇÃO DA TELA /NOME DA JANELA(GAME)/ CARREGAR A IMAGEM DO map/ SETAR O ICONE DO JOGO NA ABA
IconePokebola = pg.image.load("Componentes/HUD/Recursos/Coletados/Pokebola.png")
IconePokebola = pg.transform.smoothscale(IconePokebola, (30, 30))

# --> PONTUAÇÃO DO JOGO
NumeroPokebolas = 10
FontePokebolas = pg.font.Font("freesansbold.ttf", 25)
PokebolasColetadas = FontePokebolas.render(str(NumeroPokebolas), True, (255, 255, 255))