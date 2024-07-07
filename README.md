# Books Library

This project is a Book Management System that allows users to manage books and reviews. It includes a RESTful API built with FastAPI and a book recommendation system using KNN.

## Prerequisites

- Python 3.7+
- MongoDB (either a local installation or MongoDB Atlas)
- pip (Python package installer)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/book-management-system.git
cd book-management-system
```

###  2. Install dependencies
```bash 
pip install -r requirements.txt
```

### 3.  Set up MongoDB
- If you haven't already, set up a MongoDB instance either locally or using MongoDB Atlas.
- Update the MONGO_DETAILS variable in database.py with your MongoDB connection string.

### 4. Run the FastAPI server
```bash
uvicorn main:app --reload
```

## API Endpoints

### Authentication

Use Basic Authentication for the protected endpoints. The default username is `user` and the default password is `password`.

### Testing results
The Api endpoints testing result and document can be found here : 

### Testing with Postman
- Install Postman from here.
- Create a new request in Postman.
- Set the request type (GET, POST, PUT, DELETE) and the URL (e.g., http://127.0.0.1:8000/books).
- Set the authorization type to Basic Auth and provide the username and password (user and password).
- For POST and PUT requests, go to the Body tab, select raw, and set the format to JSON
- Enter the request body as specified above.
- Send the request and check the response.

---

## Book Recommendation System
The recommendation system uses KNN to recommend books based on genres and ratings. The data is loaded from MongoDB.

### Example Usage

```
import asyncio
from recommender import BookRecommender

book_recommender = BookRecommender()

async def main():
    await book_recommender.prepare_data()
    recommendations = book_recommender.recommend_books_by_title('Harry Potter', min_rating=4.0)
    print(recommendations)

asyncio.run(main())
```