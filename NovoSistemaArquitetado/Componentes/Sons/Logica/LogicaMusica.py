import pygame as pg

# --> INICIALIZAÇÃO E O CARRREGAMENTO DA MÚSICA DE FUNDO  ((PS: TÁ DANDO UNS BUGS VOU ARRUMAR DPS BY: SEVE))
pg.mixer.init()
pg.mixer.music.load("Componentes/Sons/Recursos/BackgroundMusic.mp3")
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.1)