# app/models.py
from pydantic import BaseModel
from typing import List

class Card(BaseModel):
    shape: str
    color: str
    number: int
    shading: str

class GameState(BaseModel):
    deck: List[Card]
    selected_cards: List[Card]
    score: int
