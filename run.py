from project.config import config
from project.models import Movie, Director, Genre, User
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Movie": Movie,
        "Director": Director,
        "Genre": Genre,
        "User": User
    }
