# app/routes/game.py
from typing import List
from fastapi import APIRouter
from app.models import GameState, Card
from app.game_logic import check_set, draw_cards

router = APIRouter()

@router.get("/game/state", response_model=GameState)
async def get_game_state():
    # 게임 상태 반환
    return GameState(deck=[], selected_cards=[], score=0)

@router.post("/game/check-set", response_model=bool)
async def check_cards(cards: List[Card]):
    # 전달받은 카드들로 Set을 검사
    return check_set(cards)

@router.post("/game/draw", response_model=List[Card])
async def draw_new_cards(deck: List[Card]):
    # 덱에서 3장의 카드를 뽑아오는 엔드포인트
    return draw_cards(deck)
