from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List
from pydantic import BaseModel, Field
from bson import ObjectId
from bson.errors import InvalidId
from recommender import BookRecommender 
import motor.motor_asyncio
from database import books_collection, reviews_collection, merged_review_collection
from database import client 

app = FastAPI()
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


async def startup_db_client():
    await client.server_info()
    print("Connected to MongoDB")

async def shutdown_db_client():
    await client.close()
    print("MongoDB connection closed")

app.add_event_handler("startup", startup_db_client)
app.add_event_handler("shutdown", shutdown_db_client)


# Basic authentication
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "user"
    correct_password = "password"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return credentials.username

def parse_objectid(id: str):
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID format")


@app.get("/")
async def root():
    return {"message": "Welcome to our library"}

@app.post("/books", response_model=Book)
async def add_book(book: Book, username: str = Depends(get_current_user)):
    book_dict = book.dict()
    result = await books_collection.insert_one(book_dict)
    book_dict["_id"] = str(result.inserted_id)
    return book_dict

@app.get("/books", response_model=List[Book])
async def get_books():
    books = await books_collection.find().to_list(1000)
    return books

@app.get("/books/{id}", response_model=Book)
async def get_book(id: str):
    try:
        book_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    book = await books_collection.find_one({"_id": book_id})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return Book(**book)

@app.put("/books/{id}", response_model=Book)
async def update_book(id: str, book: Book, username: str = Depends(get_current_user)):
    book_id = parse_objectid(id)

    result = await books_collection.update_one({"_id": book_id}, {"$set": book.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return book.dict()



@app.delete("/books/{id}")
async def delete_book(id: str, username: str = Depends(get_current_user)):
    book_id = parse_objectid(id)
    result = await books_collection.delete_one({"_id": book_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}

@app.post("/books/{id}/reviews", response_model=Review)
async def add_review(id: str, review: Review, username: str = Depends(get_current_user)):
    book_id = parse_objectid(id)

    review_dict = review.dict()
    review_dict["book_id"] = book_id
    result = await reviews_collection.insert_one(review_dict)
    review_dict["_id"] = str(result.inserted_id)

    return review_dict

@app.get("/books/{id}/reviews", response_model=List[Review])
async def get_reviews(id: str):
    book_id = parse_objectid(id)
    reviews = await reviews_collection.find({"book_id": book_id}).to_list(1000)
    return reviews

@app.get("/books/{id}/summary")
async def get_summary(id: str):
    book_id = parse_objectid(id)
    book = await books_collection.find_one({"_id": book_id})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    reviews = await reviews_collection.find({"book_id": book_id}).to_list(1000)
    if not reviews:
        raise HTTPException(status_code=404, detail="No reviews found for this book")
    
    avg_rating = sum(review["rating"] for review in reviews) / len(reviews)
    return {"summary": book["summary"], "average_rating": avg_rating}

@app.get("/recommendations/{title}")
async def get_recommendations(title:str):
    print('titile is',title)
    book = await merged_review_collection.find_one({"title": title})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book_recommender = BookRecommender()
    book_recommender.train_model()
    recommended_books_by_title = book_recommender.recommend_books_by_title(str(title), min_rating=4.0)
    
    return recommended_books_by_title
