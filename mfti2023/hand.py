from card import Card
from deck import Deck


class hand:
    def __init__(self, arr=[]):  # конструктор, передаем игроку карты на руку
        if len(arr) > 0:
            self.cards = arr
        else:
            raise ValueError("Передана пустая колода")
            None

    def __repr__(self):  # Показывает карты игрока
        print(len(self.cards))

    def quit(self):  # Выбросить карту    Проверить на удаление из массива self.cards
        if len(self.cards) > 0:
            e = self.cards.pop()
            return e
        else:
            raise ValueError("Конец ИГРЫ")
            #print()  # --------------------------------------------------------

    def into(self, arr):  # принимает массив карт
        for i in arr:
            self.cards.insert(0, i)

    def endgame(self):
        if len(self.cards) == 0:
            return 0
        return 2