import pygame as pg
import random
from settings import *
from func import *
pg.init()
print(player_img.get_size())
pg.display.set_icon(icon_img)
display.blit(bg_img, (0, 0))        # image.tr

# random.seed(77)
enemy_create()
running = True
while running:
    game_alive = model_update()
    display_redraw(game_alive)
    running, game_alive = event_processing()

pg.quit()