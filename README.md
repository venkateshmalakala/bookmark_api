# 📑 Bookmark Manager REST API

A simple RESTful API built using **Python, FastAPI, SQLModel, and SQLite** for managing personal bookmarks.  
This API implements full CRUD (Create, Read, Update, Delete) operations on a single resource and stores data persistently using a local SQLite database.

---

## 🚀 Features

- Create, read, update, and delete bookmarks
- RESTful API design
- Input validation for URL and title
- Proper HTTP status codes
- SQLite-based persistent storage
- Automatic database and table creation on startup

---

## 🛠️ Technology Stack

- **Language:** Python 3.9+
- **Framework:** FastAPI
- **ORM:** SQLModel
- **Database:** SQLite (`bookmarks.db`)
- **Server:** Uvicorn

---

## 📂 Project Structure


project-folder/
├── main.py
├── bookmarks.db       
├── requirements.txt
└── README.md


> `bookmarks.db` is automatically created when the server starts.

---

## 📦 Installation Requirements

- Python 3.9 or higher

Install dependencies:

```bash
pip install fastapi sqlmodel uvicorn
````

---

## ▶️ Running the Application

Start the server using:

```bash
uvicorn main:app --reload
```

Server URL:

```
http://127.0.0.1:8000
```

---

## 📘 API Documentation

FastAPI automatically generates interactive documentation:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧱 Data Model

Each bookmark contains the following fields:


id          - Integer (Primary Key, Auto-generated)
url         - String (Required, must start with http:// or https://)
title       - String (Required, cannot be empty)
description - String (Optional)
created_at  - Datetime (Auto-generated)

---

## 🌐 API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint        | Description        | Status Codes |
| ------ | --------------- | ------------------ | ------------ |
| POST   | /bookmarks      | Create a bookmark  | 201, 400     |
| GET    | /bookmarks      | Get all bookmarks  | 200          |
| GET    | /bookmarks/{id} | Get bookmark by ID | 200, 404     |
| PUT    | /bookmarks/{id} | Update bookmark    | 200, 400,404 |
| DELETE | /bookmarks/{id} | Delete bookmark    | 204, 404     |

---

## ➕ Create Bookmark

**POST** `/bookmarks`

Request Body:

```json
{
  "url": "https://example.com",
  "title": "Example",
  "description": "Sample bookmark"
}
```

Responses:

* `201 Created` – Bookmark created successfully
* `400 Bad Request` – Invalid URL or empty title

---

## 📄 Get All Bookmarks

**GET** `/bookmarks`

Response Example:

```json
[
  {
    "id": 1,
    "url": "https://example.com",
    "title": "Example",
    "description": "Sample bookmark",
    "created_at": "2025-01-01T10:30:00"
  }
]
```

---

## 🔍 Get Bookmark by ID

**GET** `/bookmarks/{id}`

Responses:

* `200 OK` – Bookmark returned
* `404 Not Found` – Bookmark does not exist

---

## ✏️ Update Bookmark

**PUT** `/bookmarks/{id}`

Request Body:

```json
{
  "url": "https://updated.com",
  "title": "Updated Title",
  "description": "Updated description"
}
```

Responses:

* `200 OK` – Bookmark updated
* `400 Bad Request` – Invalid input
* `404 Not Found` – Bookmark not found

---

## 🗑️ Delete Bookmark

**DELETE** `/bookmarks/{id}`

Responses:

* `204 No Content` – Bookmark deleted successfully
* `404 Not Found` – Bookmark not found

---

## ✅ Input Validation

* `title` must not be empty
* `url` must start with `http://` or `https://`
* Invalid data returns `400 Bad Request`

---

## ❗ Error Handling

* 400 – Bad Request (invalid input)
* 404 – Resource not found
* Server handles unexpected errors gracefully

---

## 💾 Data Persistence

* Data is stored in `bookmarks.db`
* Database persists across server restarts
* Tables are created automatically at startup

---

## 🎯 Learning Outcomes

* RESTful API fundamentals
* CRUD operations
* FastAPI framework usage
* SQLModel ORM basics
* SQLite database persistence

---

## ✅ Conclusion

This project demonstrates a clean and functional REST API with proper structure, validation, persistence, and documentation. It is suitable for academic submission, internships, and backend development practice.


