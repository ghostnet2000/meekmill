======
book
======
Simple book Django app.

Installation
============

(1) Install requirements:

    .. code-block:: sh

        pip install -r requirements.txt

(2) Create database:

    .. code-block:: sh

        ./manage.py migrate

(3) Collect statics:

    .. code-block:: sh

        ./manage.py collectstatic --noinput

Implementation details
======================

- For formsets Django's standard formsets functionality is used, along with
  third-party package `django-formset-js


Usage
=====

Run the project
---------------

.. code-block:: sh

    ./manage.py runserver

Public application flow
-----------------------

(1) Create Admin user

    .. code-block:: sh

        ./manage.py createsuperuser

    .. code-block:: text

        username: admin
        email: admin@localhost
        password: test1234

(2) Create Tester user

    .. code-block:: sh

        ./manage.py createsuperuser

    .. code-block:: text

        username: tester
        email: tester@localhost
        password: test1234

(3) Log in as Admin

    Navigate to http://localhost:8000/admin/ and enter Admin user credentials.

    Navigate to http://localhost:8000/ and click on the right "Add Book"
    link in the top right corner.

    Fill in a book data Then presssubmit. If all goes well, you'll be redirected to the listing of books.
    Go to books admin http://localhost:8000/admin/books/book/ and check
    the newly created book. If all goes well, you'll see.

    Create a couple of more books.


    Then proceed to the next step.

(4) Log in as Tester

    Open another (incognito) window, navigate to http://localhost:8000/admin/
    and enter Tester user credentials.

    Navigate to http://localhost:8000/ then go to a couple of detail pages
    and rate the books.


Admin application
-----------------

All of the models are editable in the admin. Navigate to the
http://localhost:8000/admin/ and see the list of available options.


/api/books/

The book endpoint for saving incoming Book data.
POST

Sample POST request:

POST http://127.0.0.1:8000/api/books/

Data/payload:

{
    "title": "fjgjf",
    "author": "kkffgjfgk",
    "description": "dkfffdkkj",
    "year": "1981",
    "image": "http://35.196.174.115:8001/media/images/image10.jpeg"
},