# app/__init__.py
from fastapi import FastAPI
from app.routes import game

app = FastAPI()

# 게임 API 라우트 연결
app.include_router(game.router)
