from deck import Deck
from card import Card

# Тест создания пустой колоды
def test_deck_init_empty():
    try:
        deck = Deck([])
        # Если исключение не было вызвано, тест не пройден
        assert False
    except Exception as e:
        assert str(e) == "Передана пустая колода"

# Тест создания колоды с картами
def test_deck_init_with_cards():
    card1 = Card('apple', 1)
    card2 = Card('lime', 2)
    card3 = Card('banana', 3)
    cards = [card1, card2, card3]
    deck = Deck(cards)
    assert deck.cards == cards

# Тест представления колоды
def test_deck_repr():
    card1 = Card('apple', 1)
    card2 = Card('lime', 2)
    card3 = Card('banana', 3)
    cards = [card1, card2, card3]
    deck = Deck(cards)
    assert deck.__repr__() == repr(cards)

# Тест перемешивания колоды
def test_deck_shuffle():
    card1 = Card('apple', 1)
    card2 = Card('lime', 2)
    card3 = Card('banana', 3)
    cards = [card1, card2, card3]
    deck = Deck(cards)
    deck.shuffle()
    assert deck.cards == cards

# Тест раздачи карт из колоды для двух игроков
def test_deck_give_2_players():
    card1 = Card('apple', 1)
    card2 = Card('lime', 2)
    card3 = Card('banana', 3)
    card4 = Card('plum', 4)
    card5 = Card('lime', 5)
    cards = [card1, card2, card3, card4, card5]
    deck = Deck(cards)
    arr1, arr2 = deck.give(2)
    assert len(arr1) == 2
    assert len(arr2) == 3

# Тест раздачи карт из колоды для недопустимого количества игроков
def test_deck_give_invalid_number():
    try:
        card1 = Card('apple', 1)
        card2 = Card('lime', 2)
        card3 = Card('banana', 3)
        card4 = Card('plum', 4)
        card5 = Card('lime', 5)
        cards = [card1, card2, card3, card4, card5]
        deck = Deck(cards)
        arr1, arr2 = deck.give(3)
        # Если исключение не было вызвано, тест не пройден
        assert False
    except Exception as e:
        assert str(e) == "Введено недопустимое значение"

test_deck_init_empty()
test_deck_init_with_cards()
test_deck_repr()
test_deck_shuffle()
test_deck_give_2_players()
test_deck_give_invalid_number()