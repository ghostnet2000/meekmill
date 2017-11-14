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
- For ratings the package `django-star-ratings
  <https://pypi.python.org/pypi/django-star-ratings>`_ is used.
- For formsets Django's standard formsets functionality is used, along with
  third-party package `django-formset-js
  <https://pypi.python.org/pypi/django-formset-js>`_ which is responsible for
  handling the JavaScript addition/removal of ingredients.

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

    Fill in a book data, add ingredient and make sure to press "Add another"
    button a couple of times, so that more formsets are created. Then press
    submit. If all goes well, you'll be redirected to the listing of books.
    Go to books admin http://localhost:8000/admin/books/book/ and check
    the newly created book. If all goes well, you'll see it along with
    all ingredients created.

    Create a couple of more books.

    Go to the detail page of each book and rate it (press the stars).

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

