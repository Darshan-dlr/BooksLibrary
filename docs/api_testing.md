# API Testing Documentation

This document provides an overview of the API endpoints and includes screenshots of tests conducted for each endpoint.

## Endpoints

### 1. Books Endpoint

#### Endpoint Details

- **URL:** `/books`
- **Methods:** POST, GET, PUT, DELETE

#### Testing

1. **POST /books**
   - **Request:** Add a new book to the library.
   - **Screenshot:**
     ![POST /books / PostMan](BooksLibrary/docs/images/postman/postReviewPm.PNG)
     ![POST /books / Mongo](BooksLibrary/docs/images/mongo/postBooksMongo.PNG)

2. **GET /books**
   - **Request:** Retrieve all books from the library.
   - **Screenshot:**
     ![GET /books](BooksLibrary/docs/images/postman/getBooksPM.PNG)

2. **GET /books/id**
   - **Request:** Retrieve a specific book from the library using the passed ID.
   - **Screenshot:**
    _Incase of invalid objectId_
     ![GET /books/{id} / postMan](BooksLibrary/docs/images/postman/getBookNotFoundPM.PNG)
     ![GET /books/{id} / Mongo](BooksLibrary/docs/images/mongo/getBookNotFoundMongo.PNG)
    _Incase of Valid objectId_
     ![GET /books/{id} / postMan](BooksLibrary/docs/images/postman/getBookFoundPM.PNG)


3. **PUT /books/{id}**
   - **Request:** Update a book's information by ID.
   - **Screenshot:**
   _Before Update_
     ![PUT /books/{id} / Mongo Bf](BooksLibrary/docs/images/mongo/putBookBeforeUpdateMongo.PNG)
   _After Update_
     ![PUT /books/{id} / Mongo Af](BooksLibrary/docs/images/mongo/putBookAfterUpdateMongo.PNG)
     ![PUT /books/{id} / PostMan Af](BooksLibrary/docs/images/postman/putBookAfterUpdatePM.PNG)

4. **DELETE /books/{id}**
   - **Request:** Delete a book by ID.
   - **Screenshot:**
   _Before deleting_
     ![DELETE /books/{id} /postman](BooksLibrary/docs/images/mongo/beforeDelete.PNG)

   _After deleting_
     ![DELETE /books/{id} /postman](BooksLibrary/docs/images/postman/PostDelete.PNG)

### 2. Reviews Endpoint

#### Endpoint Details

- **URL:** `/books/{id}/reviews`
- **Methods:** POST, GET

#### Testing

1. **POST /books/{id}/reviews**
   - **Request:** Add a review for a specific book.
   - **Screenshot:**
     ![POST /books/{id}/reviews / Mongo](BooksLibrary/docs/images/mongo/postReviewMongo.PNG)
     ![POST /books/{id}/reviews / PostMan](BooksLibrary/docs/images/postman/postReviewPm.PNG)


2. **GET /books/{id}/reviews**
   - **Request:** Retrieve all reviews for a specific book.
   - **Screenshot:**
     ![GET /books/{id}/reviews](BooksLibrary/docs/images/postman/getBookSummaryPM.PNG)

### 3. Recommendations Endpoint

#### Endpoint Details

- **URL:** `/recommendations/{title}`
- **Methods:** GET

#### Testing

**Screenshot recommendations output**
     ![recommendations](C:\Users\devarajud\Desktop\gitCodes\BooksLibrary\docs\images\recommender.PNG)


1. **GET /recommendations/{title}**
   - **Request:** Get book recommendations based on a book title.
   - **Screenshot:** WIP

