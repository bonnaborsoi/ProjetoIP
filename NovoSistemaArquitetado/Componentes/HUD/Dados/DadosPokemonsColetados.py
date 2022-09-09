import pygame as pg
pg.init()

# --> INICIALIZAÇÃO DA TELA /NOME DA JANELA(GAME)/ CARREGAR A IMAGEM DO map/ SETAR O ICONE DO JOGO NA ABA
IconePokemon = pg.image.load("Componentes/HUD/Recursos/Pikachu.png")
IconePokemon = pg.transform.smoothscale(IconePokemon, (30, 30))

# --> PONTUAÇÃO DO JOGO
NumeroPokemons = 0
FontePokemons = pg.font.Font("freesansbold.ttf", 25)
PokemonsColetados = FontePokemons.render(str(NumeroPokemons), True, (255, 255, 255))