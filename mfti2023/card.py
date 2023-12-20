


class Card:
    FRUITS = ['apple', 'lime', 'banana', 'plum']  # Задаем Фрукты (аналог цветам карт)
    NUMBERS = list(range(1, 6))  # Количество фруктов от 1 до 5
    FRUIT_LETTER = {'a': 'apple', 'l': 'lime', 'b': 'banana', 'p': 'plum'}

    def __init__(self, fruit, number):
        if fruit in self.FRUITS:  # Если цвет существует
            self.fruit = fruit  # Цвет карты = заданному
        else:
            raise ValueError(f'Wrong fruit {fruit}')

        if number in Card.NUMBERS:  # Если номер в нормальных пределах
            self.number = number
        else:
            raise ValueError(f'Wrong number {number}')

    def __repr__(self):  # Возвращаем значение цвета и номера
        return f'{self.fruit[0]}{self.number}'

    def __eq__(self, other):  # Проверка карт на одинаковость
        return self.fruit == other.fruit and self.number == other.number

    @staticmethod
    def create(text: str):
        """ По тексту вида 'r4' возвращается карта Card('red', 4)."""
        letter = Card.FRUIT_LETTER.get(text[0], None)
        number = int(text[1:])
        return Card(letter, number)

    def five(self, other):  # Проверяем, дают ли 2 карты одного номинала 5
        return (other.number + self.number == 5) and (other.fruit == self.fruit) or ((self.number == 5 and other.number != 5) and (self.fruit != other.fruit)) or ((self.number != 5 and other.number == 5) and (self.fruit != other.fruit)) or ((self.number == 5 and other.number == 5) and (self.fruit != other.fruit))

    def create_d(self, cards=[]):
        if len(cards) == 0:
            for e in range(2):
                for i in ['a', 'l', 'b', 'p']:
                    for j in range(1, 6):
                        cards.append(Card.create(str(i) + str(j)))
        else:
            print("Колода уже создана")
        return cards