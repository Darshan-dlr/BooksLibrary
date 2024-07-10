# tests/test_main.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.main import Book, Review

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup():
    # Optional: Setup any fixtures needed for testing
    pass

def test_add_book():
    new_book = {
        "title": "New Book",
        "author": "Author Name",
        "genre": ["Fantasy", "Adventure"],
        "year_published": 2023,
        "summary": "Summary of the new book."
    }
    response = client.post("/books", json=new_book)
    assert response.status_code == 200
    assert response.json()["title"] == new_book["title"]

# def test_update_book():
#     book_id = 1  # Replace with a valid book ID from your database
#     updated_book_data = {
#         "title": "Updated Book Title",
#         "author": "New Author Name",
#         "genre": ["Fantasy"],
#         "year_published": 2023,
#         "summary": "Updated summary of the book."
#     }
#     response = client.put(f"/books/{book_id}", json=updated_book_data)
#     assert response.status_code == 200
#     assert response.json()["title"] == updated_book_data["title"]

# def test_delete_book():
#     book_id = 1  # Replace with a valid book ID from your database
#     response = client.delete(f"/books/{book_id}")
#     assert response.status_code == 200
#     assert response.json()["message"] == f"Book with ID {book_id} deleted successfully."

def test_add_review():
    book_id = '668ad5f90b1c65eab772091d'  # Replace with a valid book ID from your database
    new_review = {
        "user_id": 1214900281949712947,
        "review_text": "This book was amazing!",
        "rating": 5.0
    }
    response = client.post(f"/books/{book_id}/reviews", json=new_review)
    assert response.status_code == 200
    assert response.json()["review_text"] == new_review["review_text"]

# def test_get_book_summary():
#     book_id = 1  # Replace with a valid book ID from your database
#     response = client.get(f"/books/{book_id}/summary")
#     assert response.status_code == 200
#     assert "summary" in response.json()
