import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Fixture for the FastAPI test client."""
    return TestClient(app)


def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Books Library Management System"}


def test_add_book(client):
    """Test adding a new book."""
    new_book = {
        "title": "New Book",
        "author": "Author Name",
        "genre": ["Fiction"],
        "year_published": 2022,
        "summary": "A new fictional book.",
    }
    response = client.post("/books", json=new_book)
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_book(client):
    """Test retrieving a book by ID."""
    book_id = "some-mock-id"
    response = client.get(f"/books/{book_id}")
    assert response.status_code in [200, 404]  # Test for both existing and non-existing IDs


def test_recommend_books(client):
    """Test the book recommendation endpoint."""
    payload = {
        "genres": ["Fantasy"],
        "min_rating": 4.0,
        "num_recommendations": 5,
    }
    response = client.post("/recommendations", json=payload)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_authentication(client):
    """Test authentication for a protected endpoint."""
    response = client.get("/protected", headers={"Authorization": "Basic Sm9lOmxpYnJhcmlhbg=="})
    assert response.status_code == 200
    assert response.json() == {"message": "Authenticated"}
