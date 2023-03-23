# TODO: Feature 1
from flask import Flask
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
import pytest

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

    @pytest.fixture()
    def client(app):
        return app.test_client()
    
    @pytest.fixture()
    def runner(app):
        return app.test_cli_runner()

    test_movie = Movie('Tenet', 10)
    
    def test_get_all_movies(client):
        movie = movie_repo.create_movie('Tenet', 10)
        assert response.status_code == 200
        return (str(movie_title)": "(int(movie_rating)/10))

    def test_get_all_movies(client):
        movie = movie_repo.create_movie(100, -4)
        assert response.status_code == 200
        assert b'404 NOT FOUND' in response.body
        return (str(movie_title)": "(int(movie_rating)/10))

