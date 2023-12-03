import pygame as pg
from deck import Deck
from hand import hand
def main():
    pass
if __name__ == '__main__':
    main()


SW = 1050  # размер экрана
SH = 600
screen = pg.display.set_mode((SW, SH))


FPS = 30

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
v_rez_img = pg.image.load(r'../img/doska_rez.png')
pvp_img = pg.image.load(r'../img/PvP.png')
vsPC_img = pg.image.load(r'../img/vsPC.png')
cross_img = pg.image.load(r'../img/cross.png')
g_field_img = pg.image.load(r'../img/game_field_stock.png')
card_img = pg.image.load(r'../img/card_empt.png')