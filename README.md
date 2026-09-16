# Employee Management System

## 1. Project Overview

The Employee Management System is a web-based CRUD application developed to manage employee information in a simple and organized way.

The application allows users to add new employee records, view existing records, update employee details, delete records, and search for employees by name.

The frontend is developed using HTML, CSS, and JavaScript. The backend is developed using Python and Django REST Framework. SQLite is used as the database for storing employee information.

## 2. Problem Statement

Managing employee information manually can be time-consuming and may lead to errors or difficulty in maintaining records.

This project provides a simple web-based system to store and manage employee information efficiently. It performs CRUD operations through a user-friendly interface and REST API.

## 3. Objectives

- To develop a simple Employee Management System.
- To implement Create, Read, Update, and Delete operations.
- To store employee information in a database.
- To provide a REST API for employee records.
- To provide search functionality.
- To validate user input.
- To connect the frontend with the backend API.
- To test the application using Postman.

## 4. Features

- Add new employee records.
- View all employee records.
- View individual employee details.
- Update employee information.
- Delete employee records.
- Search employees by name.
- Email validation.
- Required field validation.
- Unique email validation.
- REST API support.
- SQLite database storage.

## 5. Employee Information

The system stores the following employee details:

| Field | Description |
|---|---|
| ID | Unique employee ID |
| Name | Employee name |
| Email | Employee email address |
| Phone | Employee phone number |
| Department | Employee department |
| Position | Employee job position |
| Salary | Employee salary |

## 6. Technologies Used

| Technology | Purpose |
|---|---|
| HTML | Creates the structure of the webpage |
| CSS | Provides styling for the webpage |
| JavaScript | Handles frontend functionality and API requests |
| Python | Backend programming language |
| Django | Web framework |
| Django REST Framework | Creates REST API |
| SQLite | Database |
| Git | Version control |
| GitHub | Source code repository |
| VS Code | Development environment |
| Postman | API testing |

## 7. System Architecture

The application follows a simple frontend-backend-database architecture.

User
↓
HTML + CSS + JavaScript
↓
Django REST API
↓
Django ORM
↓
SQLite Database

The user interacts with the web interface. HTML and CSS provide the webpage structure and design. JavaScript sends requests to the Django REST API. Django REST Framework processes the API requests and Django ORM communicates with the SQLite database. The database stores employee records and the response is returned to the frontend.

## 8. Database Design

The project uses SQLite as the database.

Employee Table:

| Field | Constraint |
|---|---|
| id | Primary Key |
| name | Required |
| email | Unique |
| phone | Required |
| department | Required |
| position | Required |
| salary | Required |

Database constraints include a primary key for employee ID, unique email addresses, required employee fields, and valid email format validation.

## 9. CRUD Operations

CRUD stands for Create, Read, Update, and Delete.

### Create

A new employee can be added by entering employee details in the form and clicking the Save Employee button.

### Read

The application retrieves employee records from the REST API and displays them in a table.

### Update

The Edit button loads the selected employee's details into the form. The user can modify the details and save the changes.

### Delete

The Delete button removes the selected employee record after confirmation.

## 10. Search Functionality

The application provides a search box to find employees by name.

When the user enters a name, JavaScript filters the employee records and displays the matching records.

## 11. REST API

The backend provides REST API endpoints for employee management.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /api/employees/ | Get all employees |
| POST | /api/employees/ | Create a new employee |
| GET | /api/employees/{id}/ | Get one employee |
| PUT | /api/employees/{id}/ | Update an employee |
| DELETE | /api/employees/{id}/ | Delete an employee |

## 12. API Testing

The REST API was tested using Postman.

| Operation | Method | Result |
|---|---|---|
| View employees | GET | 200 OK |
| Create employee | POST | 201 Created |
| Update employee | PUT | 200 OK |
| Delete employee | DELETE | 204 No Content |

The tests confirmed that the main CRUD API operations work correctly.

## 13. Validation

The application includes input validation to improve data accuracy.

### Frontend Validation

- Name is required.
- Email is required.
- Phone number is required.
- Department is required.
- Position is required.
- Salary is required.
- Email field checks for a valid email format.

### Backend Validation

Django REST Framework validates submitted employee data before saving it to the database.

The email field is configured as unique, preventing duplicate email records.

## 14. Project Structure

EmployeeManagement/
│
├── employee_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── employees/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── templates/
│   │   └── employees/
│   │       └── index.html
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── .gitignore
├── db.sqlite3
├── manage.py
└── README.md

## 15. Installation and Setup

### Step 1: Clone the Repository

git clone https://github.com/PreethaMS-code/EmployeeManagement.git

### Step 2: Open the Project Folder

cd EmployeeManagement

### Step 3: Create a Virtual Environment

python -m venv venv

### Step 4: Activate the Virtual Environment

For Windows:

venv\Scripts\activate

### Step 5: Install Required Packages

pip install django
pip install djangorestframework

### Step 6: Apply Database Migrations

python manage.py migrate

### Step 7: Start the Development Server

python manage.py runserver

### Step 8: Open the Application

http://127.0.0.1:8000/

REST API:

http://127.0.0.1:8000/api/employees/

## 16. Testing Procedure

The application was tested through both the web interface and Postman.

### Frontend Testing

The following operations were tested:

- Adding an employee.
- Viewing employee records.
- Updating employee details.
- Deleting an employee.
- Searching for an employee.
- Checking required fields.
- Checking invalid email input.

### API Testing

Postman was used to test the REST API independently.

The main API operations tested were GET, POST, PUT, and DELETE.

The response status codes were checked after each request.

## 17. Challenges and Solutions

### Challenge 1: Connecting Frontend and Backend

The frontend needed to communicate with the Django backend.

Solution: JavaScript Fetch API was used to send HTTP requests to the Django REST API.

### Challenge 2: Database Storage

Employee information needed to be stored permanently.

Solution: Django ORM and SQLite were used to create and manage the Employee database table.

### Challenge 3: Input Validation

Incorrect email formats and empty fields could affect data quality.

Solution: HTML validation and Django REST Framework validation were used.

### Challenge 4: API Testing

The API needed to be tested independently from the frontend.

Solution: Postman was used to test GET, POST, PUT, and DELETE requests.

## 18. Version Control

Git was used for version control during the development of the project.

The project was uploaded to GitHub for source code management and submission.

A .gitignore file was used to prevent unnecessary files such as the virtual environment and Python cache files from being tracked.

## 19. Future Enhancements

The following features can be added in future versions:

- User login and authentication.
- Role-based access control.
- Employee profile management.
- Department-wise filtering.
- Salary reports.
- Employee attendance management.
- Improved mobile responsiveness.
- Dashboard with employee statistics.
- Export employee records to CSV or PDF.

## 20. Conclusion

The Employee Management System successfully demonstrates the development of a CRUD-based web application using Django REST Framework, JavaScript, and SQLite.

The system provides a simple interface for managing employee records and supports Create, Read, Update, and Delete operations through both the web interface and REST API.

The project also demonstrates database management, input validation, API testing, frontend-backend integration, and GitHub-based version control.

## 21. Repository

GitHub Repository:

https://github.com/PreethaMS-code/EmployeeManagement

## 22. Author

Developed as part of the college Standard Operating Procedure (SOP) activity.

Project: Employee Management System

Type: CRUD-Based Web Application

Backend: Django REST Framework

Database: SQLite