"""
main.py
=======

This module defines the main application for the Books Library Management System.

It provides a RESTful API built using FastAPI, allowing users to manage books,
retrieve book summaries, generate recommendations, and manage reviews.

The module includes the following features:
- CRUD operations for books and reviews.
- Book recommendations based on genres and average ratings.
- Integration with MongoDB for data persistence.
- Basic authentication for secure access to endpoints.

Routes
------
- `/` : Health check endpoint.
- `/books` : CRUD operations for books.
- `/reviews` : CRUD operations for reviews.
- `/recommendations` : Generate book recommendations.

Authentication
--------------
Basic Authentication is used to protect endpoints, with a default username of `Joe` and a password of `librarian`.
"""

from fastapi import FastAPI, HTTPException, Depends, Path
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List
from pydantic import BaseModel, Field
from bson import ObjectId
from bson.errors import InvalidId
import motor.motor_asyncio
import logging

from .database import books_collection, reviews_collection, client
from .recommender import BookRecommender

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Books Library Management System",
    description="API for managing a library of books and reviews, with recommendations based on the genre and average rating of a provided book title.",
    version="1.0.0"
)
security = HTTPBasic()

class Book(BaseModel):
    title: str
    author: str
    genre: str
    year_published: int
    summary: str

class Review(BaseModel):
    user_id: str
    review_text: str
    rating: float

book_recommender = BookRecommender()

async def startup_db_client():
    await client.server_info()
    logging.info("Connected to MongoDB")
    await book_recommender.prepare_data() 
    logging.info("Book recommender system trained and ready")

async def shutdown_db_client():
    await client.close()
    logging.info("MongoDB connection closed")

app.add_event_handler("startup", startup_db_client)
app.add_event_handler("shutdown", shutdown_db_client)

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Authenticate the user using HTTP Basic Authentication.
    
    Args:
        credentials (HTTPBasicCredentials): HTTP Basic Authentication credentials.

    Returns:
        str: The username if authentication is successful.

    Raises:
        HTTPException: If the username or password is incorrect.
    """
    correct_username = "Joe"
    correct_password = "librarian"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return credentials.username

def parse_objectid(id: str):
    """
    Parse a string to an ObjectId.

    Args:
        id (str): The ID string to be parsed.

    Returns:
        ObjectId: The parsed ObjectId.

    Raises:
        HTTPException: If the ID format is invalid.
    """
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID format")

@app.get("/")
async def root():
    """
    Welcome endpoint.

    Returns:
        dict: A welcome message.
    """
    return {"message": "Welcome to our library"}

@app.post("/books", response_model=Book)
async def add_book(book: Book, username: str = Depends(get_current_user)):
    """
    Add a new book to the library.

    Args:
        book (Book): The book details.
        username (str): The username of the authenticated user.

    Returns:
        dict: The added book details including the ID.
    """
    book_dict = book.dict()
    result = await books_collection.insert_one(book_dict)
    book_dict["_id"] = str(result.inserted_id)
    return book_dict

@app.get("/books", response_model=List[Book])
async def get_books():
    """
    Get a list of all books in the library.

    Returns:
        List[Book]: A list of all books.
    """
    books = await books_collection.find().to_list(1000)
    return books

@app.get("/books/{id}", response_model=Book)
async def get_book(id: str = Path(..., description="The ID of the book as a valid MongoDB ObjectId")):
    """
    Get a book by its ID.

    Args:
        id (str): The ID of the book as a valid MongoDB ObjectId.

    Returns:
        Book: The book details.

    Raises:
        HTTPException: If the book is not found or the ID format is invalid.
    """
    book_id = parse_objectid(id)
    book = await books_collection.find_one({"_id": book_id})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return Book(**book)

@app.put("/books/{id}", response_model=Book)
async def update_book(
    book: Book, 
    id: str = Path(..., description="The ID of the book as a valid MongoDB ObjectId"), 
    username: str = Depends(get_current_user)
):
    """
    Update a book's details by its ID.

    Args:
        id (str): The ID of the book as a valid MongoDB ObjectId.
        book (Book): The updated book details.
        username (str): The username of the authenticated user.

    Returns:
        Book: The updated book details.

    Raises:
        HTTPException: If the book is not found or the ID format is invalid.
    """
    book_id = parse_objectid(id)
    result = await books_collection.update_one({"_id": book_id}, {"$set": book.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return book.dict()

@app.delete("/books/{id}")
async def delete_book(id: str = Path(..., description="The ID of the book as a valid MongoDB ObjectId"), username: str = Depends(get_current_user)):
    """
    Delete a book by its ID.

    Args:
        id (str): The ID of the book as a valid MongoDB ObjectId.
        username (str): The username of the authenticated user.

    Returns:
        dict: A message indicating the book was deleted.

    Raises:
        HTTPException: If the book is not found or the ID format is invalid.
    """
    book_id = parse_objectid(id)
    result = await books_collection.delete_one({"_id": book_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}

@app.post("/reviews/{book_id}", response_model=Review)
async def add_review(
    review: Review, 
    book_id: str = Path(..., description="The ID of the book as a valid MongoDB ObjectId"), 
    username: str = Depends(get_current_user)
):
    """
    Add a review to a book.

    Args:
        book_id (str): The ID of the book as a valid MongoDB ObjectId.
        review (Review): The review details.
        username (str): The username of the authenticated user.

    Returns:
        dict: The added review details including the ID.

    Raises:
        HTTPException: If the book is not found or the ID format is invalid.
    """
    book_id = parse_objectid(book_id)
    review_dict = review.dict()
    review_dict["book_id"] = book_id
    result = await reviews_collection.insert_one(review_dict)
    review_dict["_id"] = str(result.inserted_id)
    return review_dict

@app.get("/reviews/{book_id}", response_model=List[Review])
async def get_reviews(book_id: str = Path(..., description="The ID of the book as a valid MongoDB ObjectId")):
    """
    Get a list of reviews for a specific book.

    Args:
        book_id (str): The ID of the book as a valid MongoDB ObjectId.

    Returns:
        List[Review]: A list of reviews for the book.

    Raises:
        HTTPException: If the ID format is invalid.
    """
    book_id = parse_objectid(book_id)
    reviews = await reviews_collection.find({"book_id": book_id}).to_list(1000)
    return reviews

@app.get("/recommendations/{book_title}")
async def get_recommendations(book_title: str = Path(..., description="The title of the book for generating recommendations based on genre and average rating")):
    """
    Get book recommendations based on the genre and average rating of a provided book title.

    Args:
        book_title (str): The title of the book.

    Returns:
        list: A list of recommended books.
    """
    recommendations = await book_recommender.recommend_books_by_title(book_title)
    if isinstance(recommendations, str):
        raise HTTPException(status_code=404, detail=recommendations)
    return recommendations.to_dict(orient="records")
