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
<img width="748" alt="postBooksPM" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/ac0ba6b2-d26b-4dfb-8eed-c876625a1dcc">

<img width="941" alt="postBooksMongo" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/e037547a-97c0-47d2-802d-a4c927be2b13">



2. **GET /books**
   - **Request:** Retrieve all books from the library.
   - **Screenshot:**
<img width="656" alt="getBooksPM" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/6206d69a-46e4-4e29-bb47-eb2764d81a20">

2. **GET /books/id**
   - **Request:** Retrieve a specific book from the library using the passed ID.
   - **Screenshot:**
    _Incase of invalid objectId_
<img width="655" alt="getBookNotFoundPM" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/87cd623b-2c42-4cce-a007-3f80c9ebbe17">

<img width="859" alt="getBookNotFoundMongo" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/fba2c9fb-8b7a-4008-880c-a4be3a9939a8">

    _Incase of Valid objectId_

    <img width="644" alt="getBookFoundPM" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/f5ea9bc4-ce1d-465c-bd84-1be7be96b0c2">



3. **PUT /books/{id}**
   - **Request:** Update a book's information by ID.
   - **Screenshot:**
   _Before Update_
<img width="740" alt="putBookBeforeUpdateMongo" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/b23b2818-fe8c-41cb-ad61-7ca9f8380e14">

   _After Update_
<img width="733" alt="putBookAfterUpdateMongo" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/586d2a5e-fc52-4906-96cc-649dd44d4bc8">
<img width="641" alt="putBookAfterUpdatePM" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/2bc2b94d-aab6-4b75-8489-1f5d8ef8b9c1">


4. **DELETE /books/{id}**
   - **Request:** Delete a book by ID.
   - **Screenshot:**
   _Before deleting_

<img width="708" alt="beforeDelete" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/9006037f-b9e6-4dd0-ab9a-3203a157a238">

   _After deleting_

<img width="643" alt="PostDelete" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/117630b5-36cf-43a3-87c7-da88767af5c9">


### 2. Reviews Endpoint

#### Endpoint Details

- **URL:** `/books/{id}/reviews`
- **Methods:** POST, GET

#### Testing

1. **POST /books/{id}/reviews**
   - **Request:** Add a review for a specific book.
   - **Screenshot:**
<img width="724" alt="postReviewMongo" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/fe780a55-83a8-4eae-907b-99a5cf8fdf59">

<img width="641" alt="postReviewPm" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/9b070cc7-bbf2-4c9a-bba0-267901e50629">



2. **GET /books/{id}/reviews**
   - **Request:** Retrieve the reviews data for a specific book.
   - **Screenshot:**
   <img width="635" alt="getReviewspm" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/c8857fe4-19ea-4a53-9e71-901ee96f03c0">

2. **GET /books/{id}/summary**
   - **Request:** Retrieve the summary and aggregated rating for the provided book id.
   - **Screenshot:**
<img width="662" alt="getBookSummaryPM" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/30141c8f-9ba7-4322-ad8a-90c0385f4798">

### 3. Recommendations Endpoint

#### Endpoint Details

- **URL:** `/recommendations/{title}`
- **Methods:** GET

#### Testing

**Screenshot recommendations output**
     <img width="595" alt="Recommender" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/3b378bda-b37b-431e-8e73-6a9caa111115">



1. **GET /recommendations/{title}**
   - **Request:** Provide the book title based on the genre of the provided book, and also recommend the book with the highest average ratings.

Note: The displaying of matched_genres and average_rating would be removed going ahead
   - **Screenshot:** 
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/d5df316b-6a3b-4dce-9c62-b2338c1a6435)


