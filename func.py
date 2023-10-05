import pygame as pg
import random
from settings import *

def enemy_create():
    """ Создаем противника в случайном месте вверху окна."""
    global enemy_y, enemy_x
    enemy_x = random.randint(0, screen_width - enemy_width)   # screen_width / 2 - enemy_width / 2
    enemy_y = 0
    print(f'CREATE: {enemy_x=}')



def model_update():
    global game_alive
    palayer_model()
    bullet_model()
    game_alive = enemy_model()
    return game_alive

def palayer_model():
    x = 7   # создание переменной и ее инициализация
    x = 7   # изменение значения уже созданной переменнной
    global player_x
    player_x += player_dx
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

def bullet_model():
    """ Изменяется положение пули.
    """
    global bullet_y, bullet_alive
    bullet_y += bullet_dy
    # пуля улетела за верх экрана
    if bullet_y < 0:
        bullet_alive = False

def bullet_create():
    global bullet_y, bullet_x, bullet_alive
    bullet_alive = True
    bullet_x = player_x + 16  # микро дз - пускать из середины
    bullet_y = player_y - bullet_height

def enemy_model():
    """ Изменение положения противника, рассчет поражений."""
    global enemy_y, enemy_x, bullet_alive
    global player_y
    global game_alive
    global k_counter
    enemy_x += enemy_dx * 2
    enemy_y += enemy_dy * 2
    if (enemy_y + 64) > screen_height or (enemy_y + 64 >= player_y and (((enemy_x + 64) >= player_x and enemy_x < player_x + 64 ))):
        game_alive = False
###########################################
    # пересечение с пулей
    if bullet_alive:
        re = pg.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        rb = pg.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
        is_crossed = re.colliderect(rb)
        # попал!
        if is_crossed:
            print('BANG!')
            enemy_create()
            k_counter += 1
            bullet_alive = False
    return game_alive
def display_redraw(game_alive):
    global sys_font
    global k_counter
    display.blit(bg_img, (0, 0))
    if game_alive == True:
        display.blit(player_img, (player_x, player_y))
        display.blit(enemy_img, (enemy_x, enemy_y))
        display.blit(font_small.render("score: %.d"%(k_counter), True, 'white'), (0, 0))
        if bullet_alive:
            display.blit(bullet_img, (bullet_x, bullet_y))
    else:
        #print(game_alive)
        display.blit(font.render("YOU LOSE", True, 'white'), (280, 240))
        display.blit(font.render("press p to restart", True, 'white'), (150, 300))
        display.blit(font.render("score: %.d" % (k_counter), True, 'white'), (280, 180))
    pg.display.update()
def event_processing():
    global game_alive
    global player_dx
    global k_counter
    running = True
    for event in pg.event.get():
        # нажали крестик на окне
        if event.type == pg.QUIT:
            running = False
        # тут нажимаем на клавиши
        if event.type == pg.KEYDOWN:
            # нажали на q - quit
            if event.key == pg.K_q:
                running = False
        if game_alive == True:
            # движение игрока
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    player_dx = -player_velocity
                if event.key == pg.K_d or event.key == pg.K_RIGHT:
                    player_dx = player_velocity
            if event.type == pg.KEYUP:
                player_dx = 0

            # по левому клику мыши стреляем
            if event.type == pg.MOUSEBUTTONDOWN:
                key = pg.mouse.get_pressed()    # key[0] - left, key[2] - right
                print(f'{key[0]=} {bullet_alive=}')
                if not bullet_alive:
                    bullet_create()
        else:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    game_alive = True
                    k_counter = 0
                    enemy_create()
    clock.tick(FPS)
    return running, game_alive
