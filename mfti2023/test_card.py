import pytest
from card import Card


# Тест создания карты
def test_card_init():
    card = Card('apple', 3)
    assert card.fruit == 'apple'
    assert card.number == 3


# Тест представления карты как строки
def test_card_repr():
    card = Card('banana', 2)
    assert card.__repr__() == 'b2'


# Тест проверки на одинаковость двух карт
def test_card_eq():
    card1 = Card('lime', 4)
    card2 = Card('lime', 4)
    card3 = Card('banana', 2)
    assert card1.__eq__(card2) == True
    assert card1.__eq__(card3) == False


# Тест создания карты по тексту
def test_card_create():
    card = Card.create('a1')
    assert card.fruit == 'apple'
    assert card.number == 1


# Тест проверки двух карт на сумму равную пяти
def test_card_five():
    card1 = Card('apple', 2)
    card2 = Card('apple', 3)
    card3 = Card('lime', 5)
    assert card1.five(card2) == True
    assert card2.five(card3) == False


test_card_init()
test_card_repr()
test_card_eq()
test_card_create()
test_card_five()
