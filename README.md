Problem Statement: 

Flask Library Management System Objective
  
  Create a RESTful API for a library management system using Flask. This system should allow users to perform CRUD operations on books and manage user authentication and authorization.

Requirements

1. User Authentication and Authorization
   
  Implement user registration and login endpoints.
  Use JSON Web Tokens (JWT) for user authentication.
  Ensure that certain endpoints require authorization, differentiating between admin and regular users.

2. Book Management

  Implement CRUD operations for books:
  Create a new book (admin only).
  Read all books (available to all users).
  Read a single book by its ID (available to all users).
  Update book details (admin only).
  Delete a book (admin only).

3. API Endpoints
   
User Endpoints:

  POST /register:  Register a new user.
  Request body:  {"username": "string", "password": "string", "role": "string"} (role can be "admin" or "user").
  Response:  User details (without password) and a JWT token.
  POST /login:  Log in an existing user.
  Request body:  {"username": "string", "password": "string"}
  Response:  JWT token.

Book Endpoints:

  POST /books: Add a new book (admin only).
  Request body:  {"title": "string", "author": "string", "published_date": "string", "isbn": "string", "pages": "integer", "description": "string"}
  Response:  Created book details.
  GET /books:  Retrieve a list of all books.
  Response:  List of books.
  GET /books/<id>:  Retrieve details of a specific book by ID.
  Response: Book details.
  PUT /books/<id>:  Update details of a specific book by ID (admin only).
  Request body:  Any of the book fields that need to be updated.
  Response:  Updated book details.
  DELETE /books/<id>:  Delete a specific book by ID (admin only).
  Response:  Message confirming deletion.

Constraints:

  Use Flask along with Flask-JWT-Extended for handling JWT authentication.
  Use a SQLite database for storing user and book data.
  Implement proper error handling and validation for all endpoints.
  Ensure secure storage of passwords using hashing (e.g., with bcrypt).
