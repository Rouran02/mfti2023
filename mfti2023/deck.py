import random
from card import *

class Deck:
    """ Колода карт"""

    def __init__(self, cards): #конструктор, передаём ТОЛЬКО созданный список СЮДА ПОТОМ ТЕСТ
        if len(cards) > 0:
            self.cards = cards
            print("Колода создана")
        else:
            raise Exception('Передана пустая колода')
            #print('Передана пустая колода')
    def print_deck(self):
        print(self.cards)
    def shake(self): #перемешивание колоды
        random.shuffle(self.cards)

    def give(self, number):      #Раздает карты из колоды n игрокам. Реализовано - 2м. Можно расширить
        self.shake()       #перемешивает перед раздачей
        #print(self.cards)
        if number == 2:
            giv = len(self.cards)//2
            arr1 = self.cards[:giv]
            arr2 = self.cards[giv:]
            #print(giv, arr1, arr2)
            self.cards.clear() #Проверить, очищается ли!!!!!
            return arr1, arr2
        else:
            raise Exception('Введено недопустимое значение')

