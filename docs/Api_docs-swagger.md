# API Testing Documentation

This document provides an overview of the API endpoints and includes screenshots of tests conducted for each endpoint from Swagger.

The Swagger document for the endpoints can be accessed and tested using: http://127.0.0.1:8000/docs

## Endpoints

### 1. Books Endpoint

#### Books Schema
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/d9e75ce5-a2d8-4d34-baea-e73381b307fd)


#### Endpoint Details

- **URL:** `/books`
- **Methods:** POST, GET, PUT, DELETE

#### Testing

1. **POST /books**
   - **Request:** Add a new book to the library.
   - **Screenshot:**

![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/c939c984-a5da-4a6b-9a2e-6b06e3f6b60e)


_Responses_

![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/fd32b3dd-821c-4be3-a1fc-f259f9ab4e80)


2. **GET /books**
   - **Request:** Retrieve all books from the library.
   - **Screenshot:**
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/93a36afb-5511-4e3f-872d-6ab461215f2f)


2. **GET /books/id**
   - **Request:** Retrieve a specific book from the library using the passed ID.
   - **Screenshot:**

![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/3b89fd14-20c3-4bc5-a112-35d2c8c630bf)

  _Responses_
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/e7bb0495-1784-4319-8488-9fe3c3103424)



3. **PUT /books/{id}**
   - **Request:** Update a book's information by ID.
   - **Screenshot:**
   ![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/2712b6de-da1e-4f19-823c-780132c1640a)
 _Responses_
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/a4bb2aa2-4d0c-4760-8849-f3e351cc5048)

4. **DELETE /books/{id}**
   - **Request:** Delete a book by ID.
   - **Screenshot:**
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/99cff35b-3758-4201-8dbe-993f654ab5cb)
 _Responses_
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/656f42cc-952c-411e-9c55-9c725b06700d)


### 2. Reviews Endpoint

#### Reviews Schema
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/f0e724f8-0ef5-4649-9e26-821288829888)


#### Endpoint Details

- **URL:** `/books/{id}/reviews`
- **Methods:** POST, GET

#### Testing

1. **POST /books/{id}/reviews**
   - **Request:** Add a review for a specific book.
   - **Screenshot:**
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/b16d715c-6958-4816-89f5-b3ba048dd78f)
_Responses_
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/37885e21-97ea-45e3-9c78-a817ea51801e)



2. **GET /books/{id}/reviews**
   - **Request:** Retrieve the reviews data for a specific book.
   - **Screenshot:**
  ![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/3f997bb6-22a7-4f46-aa40-1ce5bc3757cb)
_Responses_
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/3ce5e1f3-8c30-4278-949d-6ec4d6f2a992)

3. **GET /books/{id}/summary**
   - **Request:** Retrieve the summary and aggregated rating for the provided book id.
   - **Screenshot:**
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/e4b8e126-1f1a-4881-9d67-95f97f22b9c4)
_Responses_
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/c510f8ad-b7a9-49db-a727-035fb4d0b685)

### 3. Recommendations Endpoint

#### Endpoint Details

- **URL:** `/recommendations/{title}`
- **Methods:** GET

#### Testing

**Screenshot recommendations output**
     <img width="595" alt="Recommender" src="https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/3b378bda-b37b-431e-8e73-6a9caa111115">



1. **GET /recommendations/{title}**
   - **Request:** Get book recommendations based on a book title.
   - **Screenshot:** WIP



_Note_: Few of the endpoints described in this document are authorized using Basic Authentication, as indicated in the image below.
![image](https://github.com/Darshan-dlr/BooksLibrary/assets/72651034/9f75a977-5524-4066-a1e1-4827f8b82037)

