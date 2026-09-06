from flask import Flask

from src.routes.movies import movies_route_bp

app = Flask(__name__)

app.register_blueprint(movies_route_bp)