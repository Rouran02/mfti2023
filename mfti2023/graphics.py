import pygame
from SET import *
from card import Card

class graphic:
    apple_img = pg.image.load(r'../img/apple.png')
    banana_img = pg.image.load(r'../img/banan.png')
    plum_img = pg.image.load(r'../img/plum.png')
    lime_img = pg.image.load(r'../img/lime.png')
    card_img = pg.image.load(r'../img/card_empt.png')
    fruit_dict = {'apple': apple_img, 'banana': banana_img, 'plum': plum_img, 'lime': lime_img}
    def __init__(self):
        self.fruit = ""
        self.number = 0

    def show_card(self, card: object, hod: int) -> int:

        if hod:
            p_x, p_y = 100, 200
            screen.blit(graphic.card_img, (p_x, p_y))
        else:
            p_x, p_y = 800, 200
            screen.blit(graphic.card_img, (p_x, p_y))

        fruit_img = graphic.fruit_dict.get(card.fruit)
        screen.blit(graphic.card_img, (p_x, p_y))
        card_img_rect = pygame.Rect(p_x, p_y, graphic.card_img.get_width(), graphic.card_img.get_height())
        c_x, c_y = card_img_rect.x + card_img_rect.width//2.7, card_img_rect.y + card_img_rect.height//2.6
        cd_x = 35
        cd_y = 40
        num_to_pos = {1: (c_x-cd_x, c_y-cd_y),
                      2: (c_x + cd_x, c_y-cd_y),
                      3: (c_x, c_y),
                      4: (c_x-cd_x, c_y + cd_y),
                      5: (c_x + cd_x, c_y + cd_y)}

        for i in range(card.number):
            pos = num_to_pos.get(i + 1)
            screen.blit(fruit_img, pos)
        pygame.display.update()
        return 0
    def card_count(self, count):
        p_x, p_y = 100, 100
        b_x, b_y = 800, 100
        screen.blit(count_card_txt.render(" " + str(count[0]) + " ", True, 'white', 'black'), (p_x, p_y))
        screen.blit(count_card_txt.render(" " + str(count[1]) + " ", True, 'white', 'black'), (b_x, b_y))
        pygame.display.update()
    def disp_update(self):
        screen.blit(g_field_img, (0, 0))
        pygame.display.update()
    def final_screen(self, num):
        if num == 0:
            screen.fill('black')
            screen.blit(count_card_txt.render("YOU LOSE", True, 'white', 'black'), (screen.get_width()//2.5, screen.get_height()//2.5))
        elif num == 1:
            screen.fill('white')
            screen.blit(count_card_txt.render("YOU WIN", True, 'black'),(screen.get_width() // 2.5, screen.get_height() // 2.5))
        pygame.display.update()