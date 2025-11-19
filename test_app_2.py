# test_app_2.py

import pytest
from app import app  # importe l’application Flask (fichier app.py, instance app)

@pytest.fixture
def client():
    """
    Configure un client de test Flask.
    """
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """
    Vérifie que la page d'accueil retourne le code 200.
    """
    response = client.get('/')
    assert response.status_code == 200, "La page d'accueil devrait retourner 200"

def test_home_content(client):
    """
    Vérifie que la page d'accueil contient un texte ou élément attendu.
    """
    response = client.get('/')
    content = response.data.decode('utf-8')
    assert '<h1>' in content or 'Bienvenue' in content, "Le contenu de la page d'accueil ne contient pas le titre attendu"

def test_nonexistent_route(client):
    """
    Vérifie que l'accès à une route non définie retourne 404.
    """
    response = client.get('/route_inexistante')
    assert response.status_code == 404, "Une route non définie devrait retourner 404"
