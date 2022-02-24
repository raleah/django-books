# django-books

##REST API built using Django REST framework on a application that sorts books.

![image](https://user-images.githubusercontent.com/83509702/155454129-0f402413-e368-499c-b678-883a41660099.png)


Built using:
  - Django
  - Django Rest Framework
  - Httpie
  - Sqlite3

## Getting Started

> 1. download this repository

Open command line and run the following commands:

> 2. cd /project-books
> 3. python -m venv books_env
> 4. .\books_env\Scripts\activate.bat
> 5. pip install Django
> 6. pip install djangorestframework
> 7. pip install httpie
> 8. start python manage.py runserver

Once installed, navigate to localhost (http://localhost:8000) in browser to see app. 

## Functionality

A serializer is used to seralize book instances into JSON. Sqlite3 is used to track instances of books in database of books.

HTTP requests can be made to the browser using httpie for API functionality. GET, POST, PUT, DELETE all supported.



