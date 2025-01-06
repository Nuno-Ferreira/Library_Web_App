# Library Web App

This project is a library web app that allows users to loan books from the library. The app is built using Django and SQLite.

## Running the web app

To run this project, you need to clone this repo locally and install the dependencies outlined in the `requirements.txt` file. You can do this by installing and creating a virtual environment:

- Clone the repo using the command `git clone https://github.com/Nuno-Ferreira/Library_Web_App.git`
- Install virtualenv using the command `pip install virtualenv`
- Create a virtual environment inside the git repository using the command `python -m virtualenv env`
- Activate the virtual environment using the command `source env/bin/activate`
- Install the dependencies using the command `pip install -r requirements.txt`

After this you can run the Django server using the command `python manage.py runserver`. This will create a database instance and then you can create a superuser to access the admin panel using the command `python manage.py createsuperuser`. You will need to create a super user to access the admin panel to add books to the library.

If you want to create other users, you can do so by following the [signup link](http://127.0.0.1:8000/signup/) on the login page.

## Features

- Users can login and register to the library
- Users can view the list of available books in the library
- Users can loan books from the library (when logged in)
- Users can view a list of other users registered in the library
- Users can view a list of books they have loaned

## Future Improvements

- Add tests to make sure functionality is working as expected
- Add date of loan when a user loans a book
- Improve UI/UX
- Redirection of users after logging in/loggin out
- Ability to return a book
- Add an admin panel to manage books and users (apart from Django admin)
- Time limit (expiration) on book loans
- Ability to request a book
- Deploy the app
