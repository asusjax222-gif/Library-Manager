# 📚 Library Inventory Manager

*A Mini Project for Programming for Problem Solving Using Python*

---

## 📝 Project Overview

This is a simple command-line based **Library Inventory Manager** designed as a first-year Python project.
The program allows users (like library staff or students) to:

* Add new books
* Issue books
* Return books
* Search for books
* View the entire library inventory
* Save data automatically in a file

Everything is done using basic Python concepts, file handling, and object-oriented programming.

---

## 🎯 Learning Objectives

By doing this project, I learned:

* How to design classes using **OOP principles**
* How to store and retrieve data using **JSON files**
* How to build a **menu-driven CLI program**
* How to handle errors with **try/except**
* How to write clean and structured code

---

## 📂 File Structure

```
LibraryProject/
│
├── library_manager.py     # Main project file
├── catalog.json           # Stores book records (auto-created)
└── README.md              # Project documentation
```

---

## 🚀 How to Run the Project

### **Step 1: Install Python**

Make sure Python 3 is installed on your computer.
Check using:

```
python --version
```

---

### **Step 2: Open the project in VS Code**

1. Open VS Code
2. Click **File → Open Folder**
3. Select the folder containing `library_manager.py`

---

### **Step 3: Run the Program**

Open the terminal in VS Code (`Ctrl + ``) and type:

```
python library_manager.py
```

You should now see:

```
=== Library Menu ===
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search by Title
6. Save & Exit
```

---

## ⚙️ Features

### ✅ Add Book

Enter title, author, and ISBN to add a new book.

### ✅ Issue Book

Marks a book as *issued* if available.

### ✅ Return Book

Marks a book as *available* again.

### ✅ View All Books

Shows a clean list of all books with their status.

### ✅ Search by Title

Finds a book by its exact title.

### ✅ Auto Save

All changes are saved into `catalog.json` when you exit.

---

## 🧠 Concepts Used

* **Classes & Objects**
* **Methods and Attributes**
* **JSON File Handling**
* **While Loops & Conditional Statements**
* **Exception Handling**
* **Basic CRUD operations (Create, Read, Update, Search)**

---

## 📌 Example Output

```
=== Library Menu ===
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search by Title
6. Save & Exit

Enter choice: 1
Title: Python Basics
Author: John Doe
ISBN: 12345
Book added successfully!
```

---

## 👤 Made By:-

**Jayesh Shrivastava**
B.Tech CSE DATA SCIENCE 
ROLL NO:- 2501420043
Programming for Problem Solving Using Python — Mini Project


