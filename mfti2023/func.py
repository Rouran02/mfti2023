import pygame as pg
from SET import *
from card import *
from deck import *
from hand import *
from table import *
def main():
    pass


if __name__ == '__main__':
    main()


def sbut(game_rz): # Обработка стартового экрана и меню
    m_pos = pg.mouse.get_pos()
    EXT = False # переменные для работы кнопок
    STRT = False
    global D
    screen.blit(bg_img, (0, 0))
    #print(m_pos)
    if (575 >= m_pos[0] >= 20 and 568 >= m_pos[1] >= 400) and game_rz == False: #кнопка старт
        screen.blit(st_but_img, (0, 393))
        STRT = True

    elif (845 >= m_pos[0] >= 688 and 252 >= m_pos[1] >= 74) and game_rz == False: #Кнопка выход
        screen.blit(ex_but_img, (684, 72))
        EXT = True

    else: # Если кнопка не нажата
        STRT = False
        EXT = False

    #if game_rz == True: #если нажата кнопка старт - вызываем меню
        #######################################

    for i in pg.event.get(): # Обработка нажатия старт/выход
        if i.type == pg.MOUSEBUTTONDOWN:
            if STRT == True:
                game_rz = 2 #при переходе к новому режиму игры создаем 2 колоды игрокам
            if EXT == True:
                exit()
        if i.type == pg.QUIT:
            exit()
    return game_rz

def ingame():
    global ingame_set
    global pl_hand
    global bot_hand
    global Tbl
    global hod
    if ingame_set == False:  #стартовые настройки игры
        screen.blit(g_field_img, (0, 0))
        screen.blit(card_img, (100, 100))
        global D
        D = Deck(Card.create_d([]))  # D - объект класса Deck, колода
        arr1, arr2 = D.give(2)
        pl_hand, bot_hand = hand(arr1), hand(arr2) #Раздача карт игрокам
        Tbl = Table() #Объект стол
        ingame_set = True #В настройки больше не заходим

    for i in pg.event.get(): # Обработка нажатия
        if i.type == pg.MOUSEBUTTONDOWN:
            None
        if i.type == pg.QUIT:
            ingame_set = False
            exit()
    pl_hand.vskryvaemsa(1)
    bot_hand.vskryvaemsa(2)
    if hod == 0: # Ходы игроков по очереди. Потом допилить, вынести часть кода в обработчик событий чтоб карты доставались по нажатию, а не автоматически
        Tbl.hod(0, pl_hand.quit())
        hod = 1
    elif hod == 1:
        Tbl.hod(1, bot_hand.quit())
        hod = 0
    Tbl.show()
    if len(Tbl.stp2) >= 1 and len(Tbl.stp1) >= 1: #переделать под нажатие кнопок и таймер
        print(Tbl.stp1[-1], Tbl.stp2[-1], Tbl.stp1[-1].five(Tbl.stp2[-1]), Tbl.sumfive())
        if Tbl.sumfive():
            if hod == 1:
                pl_hand.into(Tbl.ret())
                print("--------------------------------------------------------------FIVE, PLAYER --------------------------------------------------------------")
            elif hod == 0:
                bot_hand.into(Tbl.ret())
                print("-----------------------------------------------------------------FIVE, BOT -----------------------------------------------------------------")

    print("----------------------------------------")



def start_param(): # Начальные параметры при запуске
    global deck
    pg.display.set_caption("Hally_Gally")
    screen.blit(bg_img, (0, 0))
    pg.display.set_icon(icon_img)


