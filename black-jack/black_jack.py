"""Black Jack

https://exercism.org/tracks/python/exercises/black-jack

Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
from typing import Union

CARD_STRINGS = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """

    card = card.strip()
    if card not in CARD_STRINGS:
        return 10

    return CARD_STRINGS[card]


def higher_card(card_one: str, card_two: str) -> Union[str, tuple]:
    """Determine which card has a higher value in the hand.

    :param card_one: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :param card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """

    value_1 = value_of_card(card_one)
    value_2 = value_of_card(card_two)

    if value_2 < value_1:
        return card_one
    if value_1 < value_2:
        return card_two
    # equals
    return card_one, card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 11 (if already in hand);
        numerical value otherwise.
    :param card_two: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 11 (if already in hand);
        numerical value otherwise.
    :return: int - value of the upcoming ace card (either 1 or 11).
    """

    current_point = value_of_card(card_one) + value_of_card(card_two)
    # if 'A's in hand, one of 'A' will be 11 points.
    if card_one == 'A' or card_two == 'A':
        current_point += 10

    return 11 if current_point + 11 <= 21 else 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11;
        numerical value otherwise.
    :param card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11;
        numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    _value_1 = value_of_card(card_one)
    _value_2 = value_of_card(card_two)

    def has_ace(value_1: int, value_2: int) -> bool:
        return value_1 == 1 or value_2 == 1

    def has_ten(value_1: int, value_2: int) -> bool:
        return value_1 == 10 or value_2 == 10

    return has_ace(_value_1, _value_2) and has_ten(_value_1, _value_2)


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one: str - cards dealt.
    :param card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one: str - first and second cards in hand.
    :param card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """

    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]
