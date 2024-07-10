# Books Library

This project is a Book Management System that allows users to manage books and reviews. It includes a RESTful API built with FastAPI and a book recommendation system using KNN.

## Prerequisites

- Python 3.7+
- MongoDB (either a local installation or MongoDB Atlas)
- pip (Python package installer)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Darshan-dlr/BooksLibrary
cd BooksLibrary
```

###  2. Install dependencies
```bash 
pip install -r requirements.txt
```

### 3.  Set up MongoDB
- If you haven't already, set up a MongoDB instance either locally or using MongoDB Atlas.
- Update the MONGO_DETAILS variable in [database.py](https://github.com/Darshan-dlr/BooksLibrary/blob/5ac33b3a6d4298fee15387993bc5b8c01b490590/app/database.py#L7) with your MongoDB connection string.

_Please reach out to me for the credentials if you need to test it in the database I used during development_

### 4. Run the FastAPI server
```bash
uvicorn app.main:app --reload
```

---

## API Endpoints

### Authentication

Use Basic Authentication for the protected endpoints. The default username is `Joe` and the default password is `librarian`.

### API Documentation

Explore and test the API endpoints using the interactive Swagger UI:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
  
  Use Swagger UI to view available endpoints, input parameters, and expected responses. Click on an endpoint to expand and see details such as HTTP methods, parameters, and response codes. Use the "Try it out" button to make requests directly from the documentation interface.

- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
  
  ReDoc provides a cleaner documentation view with additional features for exploring the API.

### Testing Results and Documentation

The Api endpoints testing result and document can be found here : [api_testing.md](https://github.com/Darshan-dlr/BooksLibrary/blob/main/docs/api_testing.md)

### OpenAPI JSON File

The downloaded OpenAPI JSON file can be found in your project at [openapi.json](https://github.com/Darshan-dlr/BooksLibrary/blob/main/docs/openapi.json). Use this file to review the complete API specification.


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

### Data

The data used for the recommendation system is available as a CSV file. You can download it from the following link:

[Goodreads Books Data](https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data?resource=download)

### Setup

1. **Download the CSV file** from the link provided above.

2. **Upload the data to MongoDB**

    - Ensure MongoDB is running and accessible.
    - Use the following Python script to upload the data from the CSV file to the `merged_review` collection in your MongoDB database:

    ```python
    import pandas as pd
    from pymongo import MongoClient

    # Replace with your MongoDB connection string
    MONGO_DETAILS = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(MONGO_DETAILS)

    database = client['BooksLibrary']
    merged_review_collection = database['merged_review']

    # Load the CSV file
    file_path = 'path_to_your_csv_file.csv'
    df = pd.read_csv(file_path)

    # Insert the data into MongoDB
    data = df.to_dict(orient='records')
    merged_review_collection.insert_many(data)

    print("Data uploaded successfully!")
    ```

3. **Update `recommender.py`** with your MongoDB connection details if needed.

### Example Usage

```python
import asyncio
from recommender import BookRecommender

book_recommender = BookRecommender()

async def main():
    await book_recommender.prepare_data()
    recommendations = book_recommender.recommend_books_by_title('Harry Potter', min_rating=4.0)
    print(recommendations)

asyncio.run(main())
```

---

## License
This project is licensed under the MIT License.

## Contributing
Feel free to explore and suggest changes! You can create issues and submit pull requests on the [BooksLibrary](https://github.com/Darshan-dlr/BooksLibrary/) 
