from flask import Blueprint, request, jsonify

from src.services.get_movie import GetMovie
from src.errors.error_handler import error_handler
from src.services.redis_service import get_movies_history

movies_route_bp = Blueprint("movies_bp", __name__)

@movies_route_bp.route("/movies", methods=["POST"])
def get_movie_info():
    """
    Rota para buscarmos as informações de um filme pelo nome. Ela chama o serviço de busca, consulta as informações do filme e
    retorna esses dados.
    A rota possui um tratamento de erros, caso suba qualquer exceção ela chama o handler de exceções e repassa as
    informações detalhadas ao usuário.

    Returns:
        - dict: Contém as informações do filme ou o detalhamento do erro.
    """
    try:
        movie_service = GetMovie()
        movie_info = movie_service.consult_movie(request)

        return jsonify(movie_info)
    except Exception as ex:
        error = error_handler(ex)
        return jsonify(error["data"]), error["status_code"]

@movies_route_bp.route("/history", methods=["GET"])
def get_history():
    try:
        movies = get_movies_history()
        return jsonify(movies)
    except Exception as ex:
        error = error_handler(ex)
        return jsonify(error["data"]), error["status_code"]
