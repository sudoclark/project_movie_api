from flask import Blueprint, request, jsonify

from src.services.get_movie import GetMovie
from src.errors.error_handler import error_handler

movies_route_bp = Blueprint("movies_bp", "__filename__")

@movies_route_bp.route("/movies", methods=["POST"])
def get_movie_info():
    try:
        movie_service = GetMovie()
        movie_info = movie_service.consult_movie(request)

        return jsonify(movie_info)
    except Exception as ex:
        error = error_handler(ex)
        return jsonify(error["data"]), error["status_code"]
