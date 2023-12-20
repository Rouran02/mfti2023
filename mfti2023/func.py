import time

import pygame as pg
from SET import *
from card import Card
from deck import Deck
from hand import hand
from table import Table
import time as tm
import random as rnd
from graphics import graphic


def main():
    pass


if __name__ == '__main__':
    main()


def sbut(game_rz):  # Обработка стартового экрана и меню
    m_pos = pg.mouse.get_pos()
    # print(m_pos)
    EXT = False  # переменные для работы кнопок
    STRT = False
    global D

    screen.blit(bg_img, (0, 0))

    if (st_but_rect.collidepoint(m_pos)) and game_rz == False:  # кнопка старт
        screen.blit(st_but_img, (0, 393))
        STRT = True

    elif (ext_but_rect.collidepoint(m_pos)) and game_rz == False:  # Кнопка выход
        screen.blit(ex_but_img, (684, 72))
        EXT = True

    else:  # Если кнопка не нажата
        STRT = False
        EXT = False

    for i in pg.event.get():  # Обработка нажатия старт/выход
        if i.type == pg.MOUSEBUTTONDOWN:

            if STRT == True:
                game_rz = 2  # при переходе к новому режиму игры создаем 2 колоды игрокам

            if EXT == True:
                exit()
        if i.type == pg.QUIT:
            exit()
    return game_rz


def ingame(game_rz):
    global ingame_set
    global pl_hand
    global bot_hand
    global Tbl
    global hod
    P_KARD_OUT = False
    bot_react = rnd.uniform(1, 2.5)
    g = graphic()

    if not ingame_set:  # стартовые настройки игры
        screen.blit(g_field_img, (0, 0))
        global D
        D = Deck(Card.create_d([]))  # D - объект класса Deck, колода
        arr1, arr2 = D.give(2)
        pl_hand, bot_hand = hand(arr1), hand(arr2)  # Раздача карт игрокам
        Tbl = Table()  # Объект стол
        ingame_set = True  # В настройки больше не заходим

    pressed_space = False

    for i in pg.event.get():  # Обработка нажатия
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_m:
                P_KARD_OUT = True
        if i.type == pg.QUIT:
            ingame_set = False
            exit()

    pl_hand.__repr__()
    bot_hand.__repr__()

    if hod == 0:  # Ходы игроков по очереди.
        if P_KARD_OUT:
            try:
                Tbl.hod(0, pl_hand.quit())
                hod = 1
                graphic.show_card(Tbl.getlast(hod), Tbl.getlast(hod), hod)
            except:
                game_rz = 0
    elif hod == 1:
        try:
            tm.sleep(0.25)
            Tbl.hod(1, bot_hand.quit())
            hod = 0
            graphic.show_card(Tbl.getlast(hod), Tbl.getlast(hod), hod)
        except:
            game_rz = 0

    Tbl.show()

    graphic.card_count(g, [len(pl_hand.cards), len(bot_hand.cards)])

    if len(Tbl.stp2) >= 1 and len(Tbl.stp1) >= 1:  # переделать под нажатие кнопок и таймер3
        print(Tbl.stp1[-1], Tbl.stp2[-1], Tbl.stp1[-1].five(Tbl.stp2[-1]), Tbl.sumfive())

        if Tbl.sumfive():
            ntime = tm.time()

            while 1:
                ttime = tm.time()

                if ttime - ntime >= bot_react:
                    bot_hand.into(Tbl.ret())
                    print(
                        "-----------------------------------------------------------------FIVE, "
                        "BOT -----------------------------------------------------------------")
                    pressed_space = True
                else:
                    for event in pg.event.get():  # Обработка нажатия
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_SPACE:
                                pl_hand.into(Tbl.ret())
                                print("--------------------------------------------------------------FIVE, PLAYER "
                                      "--------------------------------------------------------------")
                                pressed_space = True
                                break
                if pressed_space:
                    graphic.disp_update(g)
                    pressed_space = False
                    break
    print("----------------------------------------")
    if pl_hand.endgame() == 0:
        game_rz = 0
        graphic.final_screen(g, 0)
        time.sleep(5)
    elif bot_hand.endgame() == 0:
        game_rz = 0
        graphic.final_screen(g, 1)
        time.sleep(5)
    return game_rz


def start_param():  # Начальные параметры при запуске
    global deck
    pg.display.set_caption("Hally_Gally")
    screen.blit(bg_img, (0, 0))
    pg.display.set_icon(icon_img)
