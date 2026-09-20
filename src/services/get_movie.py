import os
from flask import request as FlaskRequest
from dotenv import load_dotenv
import requests

from src.errors.api_key_error import ApiKeyError
from src.errors.bad_request_error import BadRequestError
from src.errors.movie_not_found import MovieNotFound
from .redis_service import add_to_history, get_movie_from_history

load_dotenv()

MOCK_API = os.getenv("API_MOCK_ENABLED", "false").lower() == "true"

class GetMovie:
    API_KEY = os.getenv("API_KEY")

    def consult_movie(self, request: FlaskRequest): # type: ignore
        """
        Método público que faz o processamento de busca do filme 
        chamando seus métodos internos especializados.

        Returns:
            - dict: Informações detalhadas do filme.
        """
        body = request.json

        movie_name = self.__verify_request(body)
        movie_history_info = get_movie_from_history(movie_name)

        if not MOCK_API:
            if movie_history_info: return movie_history_info
        
        movie_info = self.__get_movie_info(movie_name)
        response = self.__format_response(movie_info)

        if not MOCK_API:
            add_to_history(response)

        return response

    def __verify_request(self, body: dict) -> str:
        """
        Faz a validação do corpo da requisição. Valida se um body foi enviado (se não está vazio),
        se o campo "movie_name" existe na requisição e se o valor desse campo é uma string.

        Returns:
            - str: Retorna o nome do filme.

        Pode retornar um dicionário com o detalhamento da exceção em casos de erro.
        """
        if not body:
            raise BadRequestError("Dados inválidos, verifique as informações enviadas.")

        if "movie_name" not in body:
            raise BadRequestError("O nome do filme é obrigatório, verifique os dados enviados.")

        if not isinstance(body["movie_name"], str):
            raise BadRequestError("O nome do filme deve ser uma string.")

        movie_name = body["movie_name"]

        return movie_name

    def __get_movie_info(self, movie_name: str) -> dict:
        """
        Aqui é onde falamos com a API externa (OmdbAPI) para buscar as informações
        do filme solicitado. Recebe o nome (definido em __verify_request()) e 
        o usa para buscar as informações detalhadas pela API externa.

        Returns:
            - dict: Dicionário com as informações do filme ou o detalhamento do erro ocorrido.
        """
        if MOCK_API:
            return {
                "Title": "Mock title",
                "Year": "Mock released",
                "Genre": "Mock genre",
                "Director": "Mock director",
                "Plot": "Mock synopsis",
                "Actors": "Mock cast"
            }

        response = requests.get(
            f"http://www.omdbapi.com/?apikey={self.API_KEY}&t={movie_name}", timeout=5
        )
        response_data = response.json()

        if response.status_code == 401:
            raise ApiKeyError("API Key inválida, verifique as informações enviadas.")

        if response_data.get("Error") == "Movie not found!":
            raise MovieNotFound("Título do filme inválido, verifique as informações enviadas.")

        return response_data

    def __format_response(self, movie_info: dict) -> dict:
        """
        As informações que chegam da API vêm com muitos detalhes, 
        e aqui é onde nós filtramos só os dados relevantes para retornar ao usuário.

        Returns:
            - dict: Dicionário já com informações filtradas.
        """
        return {
            "title": movie_info["Title"],
            "released": movie_info["Year"],
            "genre": movie_info["Genre"],
            "director": movie_info["Director"],
            "synopsis": movie_info["Plot"],
            "cast": movie_info["Actors"]
        }
