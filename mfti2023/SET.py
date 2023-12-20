import pygame as pg
from deck import Deck
from hand import hand
def main():
    pass
if __name__ == '__main__':
    main()
pg.init()

SW = 1050  # размер экрана
SH = 600
screen = pg.display.set_mode((SW, SH))


FPS = 10

t = True  # цикл
game_rz = 0 #меню выбора режима


clock = pg.time.Clock()

ingame_set = False


#frt = ['a', 'l', 'b', 'p']

D = Deck([0]) #Колода Можно перемешивать и раздавать на 2х игроков
#arr1, arr2 = hand([]), hand([]) #колоды игроков

pl_hand = [] # Рука игрока
bot_hand = [] # Рука бота
Tbl = []
hod = 0 #очередность ходов в игре. 0 - игрок, 1 - бот

#загрузка изображений
bg_img = pg.image.load(r'../img/Start_menus.png')
icon_img = pg.image.load(r'../img/icon.png')
st_but_img = pg.image.load(r'../img/ST_B.png')
ex_but_img = pg.image.load(r'../img/EX_B.png')
g_field_img = pg.image.load(r'../img/game_field_stock.png')
card_img = pg.image.load(r'../img/card_empt.png')

st_but_rect = pg.Rect(13, 400, st_but_img.get_width(), st_but_img.get_height())
ext_but_rect = pg.Rect(689, 74, ex_but_img.get_width(), ex_but_img.get_height())

count_card_txt = pg.font.Font('../img/04B_19.TTF', 58)