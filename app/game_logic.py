# app/game_logic.py
from app.models import Card
from typing import List


def check_set(cards: List[Card]) -> bool:
    # 카드 3장의 조합이 Set인지 검사하는 로직을 여기에 구현
    # 간단한 예시: 숫자, 색상 등 3개의 조건이 모두 동일하거나 모두 다르면 Set
    return len(cards) == 3 and all(card.number == cards[0].number for card in cards)


def draw_cards(deck: List[Card]) -> List[Card]:
    # 덱에서 3장의 카드를 뽑아오는 로직을 여기에 구현
    return deck[:3]
