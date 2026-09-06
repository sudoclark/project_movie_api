from flask import request as FlaskRequest
from dotenv import load_dotenv
import requests
import os

from src.errors.api_key_error import ApiKeyError
from src.errors.bad_request_error import BadRequestError
from src.errors.movie_not_found import MovieNotFound

load_dotenv()

class GetMovie:
    API_KEY = os.getenv("API_KEY")

    def consult_movie(self, request: FlaskRequest): # type: ignore
        body = request.json

        movie_name = self.__verify_request(body)
        movie_info = self.__get_movie_info(movie_name)
        response = self.__format_response(movie_info)

        return response

    def __verify_request(self, body: dict) -> str:
        if not body:
            raise BadRequestError("Dados inválidos, verifique as informações enviadas.")

        if "movie_name" not in body:
            raise BadRequestError("O nome do filme é obrigatório, verifique as informações enviadas.")

        if not isinstance(body["movie_name"], str):
            raise BadRequestError("O nome do filme deve ser uma string.")

        movie_name = body["movie_name"]

        return movie_name

    def __get_movie_info(self, movie_name: str) -> dict:
        response = requests.get(f"http://www.omdbapi.com/?apikey={self.API_KEY}&t={movie_name}")
        response_data = response.json()

        if response.status_code == 401:
            raise ApiKeyError("API Key inválida, verifique as informações enviadas.")

        if response_data.get("Error") == "Movie not found!":
            raise MovieNotFound("Título do filme inválido, verifique as informações enviadas.")

        return response_data

    def __format_response(self, movie_info: dict) -> dict:
        return {
            "title": movie_info["Title"],
            "released": movie_info["Year"],
            "genre": movie_info["Genre"],
            "director": movie_info["Director"],
            "synopsis": movie_info["Plot"],
            "cast": movie_info["Actors"]
        }