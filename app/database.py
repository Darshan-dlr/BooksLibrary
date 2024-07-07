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
