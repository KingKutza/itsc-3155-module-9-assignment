# TODO: Feature 4
import pytest
from app import app
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()
movie_repository.clear_db()

@pytest.fixture(scope='module')
def test_app():
    return app.test_client()

def test_get_movie_by_id_proper(test_app):
    movie = movie_repository.create_movie('Spiderman', 'Sam Raimi', 10)
    id = movie.movie_id
    response = test_app.get(f'/movies/{id}')
    assert response.status_code == 200
    assert b'Spiderman' in response.data
    assert b'Sam Raimi' in response.data
    assert b'10 / 10' in response.data

def test_get_movie_by_id_improper(test_app):
    id = 1
    response = test_app.get(f'/movies/{id}')
    assert response.status_code == 200
    assert b'404 NOT FOUND!' in response.data

movie_repository.clear_db()