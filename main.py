from flask import Flask
from routes import pokemonRoutes
app = Flask(__name__)


app.register_blueprint(pokemonRoutes)



if __name__ == "__main__":
    app.run(debug=True)