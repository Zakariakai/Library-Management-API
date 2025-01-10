# 🌸 Welcome to the Library Management System API! 📚

This project is your go-to tool for managing library resources effortlessly. With this API, you can:

- **Add and manage books and users.**
- **Check books in and out with ease.**
- **Keep track of available books in real-time.**

💡 **Built with love** using Python and the Django framework, this API ensures efficiency and simplicity. 

---

### **📚 How to Install and Run the Project 🛠️**

1. **Fork the project** from GitHub and clone it to your local machine Using this :
```bash
git clone https://github.com/Haikumma/Library_Management_System.git
```
   
2. **Install dependencies:** Navigate to the project directory and install the required dependencies using pip:
```bash 
cd Library_Management_System
pip install -r requirements.txt
```

3. **Run the project** with this command:
```bash
python manage.py runserver
```

---
### **💖 How to Use the API**

Let’s dive into the magic! ✨

 **📚 Implemented Endpoints:**<br/>
**1.GET /api/books/**
  
  -**Description:** Retrieve a list of all available books.<br/>
  -**Response:** A list of books with their details (ID, title, author, availability).<br/>
  -**Example Request:**
  
  ```bash
  curl -X GET http://127.0.0.1:8000/api/books/
  ```
**2.POST /api/books/add/**

  -**Description:** Add a new book to the library.<br/>
  -**Request Body:** JSON with book title and author.
  ```bash
  {
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald"
  }
```
  -**Response**: Details of the newly added book (ID, title, author, availability).<br/>
  -**Example Request**:
  ```bash
  curl -X POST http://127.0.0.1:8000/api/books/add/ \
-H "Content-Type: application/json" \
-d '{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}'
```
**3.POST /api/checkout/**

  -**Description**: Check out a book to a user.<br/>
  -**Request Body**: JSON with book ID and user ID.<br/>
  -**Response**: Confirmation of the checkout process.<br/>
  -**Example Request**:
  
  ```bash
  curl -X POST http://127.0.0.1:8000/api/checkout/ \
-H "Content-Type: application/json" \
-d '{"book_id": 1, "user_id": 1}'
```
**4.POST /api/return/**

  -**Description**: Return a checked-out book.<br/>
  -**Request Body**: JSON with book ID.<br/>
  -**Response**: Confirmation of the return process.<br/>
  -**Example Request**:

  ```bash 
  curl -X POST http://127.0.0.1:8000/api/return/ \
-H "Content-Type: application/json" \
-d '{"book_id": 1}'
```
---
### **🌸 Additional Features**
  -**Books Management**: Add, edit, or delete books and search for your favorite titles.<br/>
  -**User Management**: Register, update, or remove users and view all library members.<br/>
  -**Checkout & Return**: Borrow books and link them to users, then return them and track their availability.<br/>
---
### **💖 How to Connect with Frontend or Use Postman**
Feel free to use Postman or connect the API to your frontend for a seamless library experience! 💖
---
### **🪄 License**
This project is under the **MIT License**.  
Feel free to **use**, **modify**, and **share** it however you like! ✨
---
### 💻**Tech Used**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
