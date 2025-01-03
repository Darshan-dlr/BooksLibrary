"""
database.py
===========

This module sets up the MongoDB connection for the Books Library Management System.

It provides asynchronous access to the database and its collections,
allowing CRUD operations and other interactions with books and reviews data.

Configuration
-------------
- MongoDB connection details are specified via the `MONGO_DETAILS` constant.
- The database is initialized as `BooksLibrary`.
- Collections:
  - `books_collection` : Stores book metadata.
  - `reviews_collection` : Stores user reviews.
  - `merged_review_collection` : Combines book and review data for recommendations.

Dependencies
------------
- `motor.motor_asyncio` : For asynchronous MongoDB interaction.

Usage
-----
Import the desired collection for database operations.

Example:
    from database import books_collection

    async def get_books():
        return await books_collection.find({}).to_list(length=None)
"""

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
import logging

logging.basicConfig(level=logging.INFO)

MONGO_DETAILS = "mongodb+srv://<user>:<password>@cluster.s.mongodb.net/?authMechanism=SCRAM-SHA-1"  # Replace with your MongoDB connection string

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.BooksLibrary
books_collection = database.get_collection("books")
reviews_collection = database.get_collection("reviews")
merged_review_collection = database.get_collection("merged_review")


try:
    client.server_info()
    logging.info("Successfully connected to MongoDB")
except ServerSelectionTimeoutError:
    logging.error("Unable to connect to MongoDB")
