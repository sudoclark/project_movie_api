from flask import Flask

from src.routes.movies import movies_route_bp

# Aqui fazemos a instanciação da aplicação Flask e registramos a rota '/movies' no app
app = Flask(__name__)

app.register_blueprint(movies_route_bp)
