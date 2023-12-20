import pygame as pg
from SET import *
from func import *

pg.init()

start_param()  # начальные параметры при запуске

while t:
    if game_rz == 0:  # Режим меню
        game_rz = sbut(game_rz)  # функция меню
    elif game_rz == 2:  # Режим игры
        game_rz = ingame(game_rz)

    clock.tick(FPS)
    pg.display.update()