import json

import redis
from dotenv import load_dotenv
import os

load_dotenv()

HISTORY_KEY = "history:movies"

redis_service = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    db=0,
    decode_responses=True
)

def add_to_history(movie: dict, max_items: int = 10) -> None:
    movie_json = json.dumps(movie)

    if redis_service.lpos(HISTORY_KEY, movie_json) is None:
        redis_service.lpush(HISTORY_KEY, movie_json)
        redis_service.ltrim(HISTORY_KEY, 0, max_items - 1)

def get_movie_from_history(movie_name: str) -> dict:
    movies_raw = redis_service.lrange(HISTORY_KEY, 0, -1)
    movies = [json.loads(item) for item in movies_raw]

    return next((movie for movie in movies if movie["title"].lower() == movie_name.lower()), None)

def get_movies_history() -> list:
    movies_raw = redis_service.lrange(HISTORY_KEY, 0, -1)
    movies = [json.loads(item) for item in movies_raw]

    return movies