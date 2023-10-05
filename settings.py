import pygame as pg
import random
pg.init()

k_counter = 0

screen_width, screen_height = 800, 600
FPS = 24    # frame per second
clock = pg.time.Clock()

game_alive = True

display = pg.display.set_mode((screen_width, screen_height))

bg_img = pg.image.load('src/background.png')
icon_img = pg.image.load('src/ufo.png')
pg.display.set_caption('Космическое вторжение')


sys_font = pg.font.SysFont('arial', 34)
font = pg.font.Font('src/04B_19.TTF', 58)
font_small = pg.font.Font('src/04B_19.TTF', 35)
text_img = sys_font.render('Score 123', True, 'white')

game_over_text = font.render('Game Over', True, 'red')
w, h = game_over_text.get_size()
# игрок
player_img = pg.image.load('src/player.png')
player_width, player_height = player_img.get_size()
player_gap = 10
player_velocity = 10
player_dx = 0
player_x = screen_width/2 - player_width/2
player_y = screen_height  - player_height - player_gap
# пуля
bullet_img = pg.image.load('src/bullet.png')
bullet_width, bullet_height = bullet_img.get_size()
bullet_dy = -5
bullet_x = 0     # микро дз - пускать из середины
bullet_y = 0
bullet_alive = False    # есть пуля?
#Враг
enemy_img = pg.image.load('src/enemy.png')
enemy_width, enemy_height = enemy_img.get_size()
enemy_dx = 0
enemy_dy = 1
enemy_x = 0
enemy_y = 0