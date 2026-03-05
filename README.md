# Student CRUD Tutorial (Flask + SQLite)

A simple web application demonstrating **basic CRUD (Create, Read,
Update, Delete) operations** using **Python Flask** and **SQLite**.

This project was created as a **learning example for Software
Engineering lab students** to understand how a web application interacts
with a database.

------------------------------------------------------------------------

## Features

-   Add new students
-   View all students
-   Edit student information
-   Delete students
-   SQLite database storage
-   Simple HTML interface

------------------------------------------------------------------------

## Project Structure

    student-crud-tutorial
    │
    ├── app.py          # Main Flask application
    ├── init_db.py      # Script to create the SQLite database
    ├── students.db     # SQLite database
    │
    └── templates       # HTML templates
        ├── index.html
        ├── add.html
        └── edit.html

------------------------------------------------------------------------

## Requirements

Make sure the following are installed:

-   Python 3
-   pip

Install Flask:

``` bash
pip install flask
```

------------------------------------------------------------------------

## Setup and Run

### 1. Clone the repository

``` bash
git clone https://github.com/YOUR_USERNAME/student-crud-tutorial.git
cd student-crud-tutorial
```

### 2. Initialize the database

``` bash
python init_db.py
```

This will create the `students.db` SQLite database.

### 3. Run the Flask application

``` bash
python app.py
```

### 4. Open in browser

    http://127.0.0.1:5000

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Flask
-   SQLite
-   HTML

------------------------------------------------------------------------

## Educational Purpose

This project is designed to help beginners understand:

-   How **web servers handle requests**
-   How **Flask routes work**
-   How **databases interact with backend applications**
-   Implementation of **CRUD operations**

------------------------------------------------------------------------

## License

This project is for **educational use**.
