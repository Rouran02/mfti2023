from card import Card
import random

class Table:
    def __init__(self):
        self.stp1 = []
        self.stp2 = []
        self.lencard = 0  # ----------------------------------------------------------

    def hod(self, player, card):  # player 0 - player, 1 - bot Добавляет карты из руки в стопки 1 или 2
        if player == 0:
            self.stp1.append(card)
        elif player == 1:
            self.stp2.append(card)

    def sumfive(self):  # Проверяет, дают ли карты в сумме 5
        if self.stp1[-1].five(self.stp2[-1]):
            return 1
        else:
            return 0

    def show(self):            # показывает все карты на столе
        print("stp1  = ", self.stp1)
        print("stp2  = ", self.stp2)

    def shake(self): #перемешивание колоды перед передачей
        random.shuffle(self.stps)
    def ret(self):
        self.stps = self.stp1 + self.stp2
        self.stp1 = []
        self.stp2 = []
        self.shake()
        return self.stps