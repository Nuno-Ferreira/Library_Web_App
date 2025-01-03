# Library Web App

This project is a library web app that allows users to loan books from the library. The app is built using Django and SQLite.

## Running the web app

To run this project, you need to clone this repo and install the dependencies outlined in the `requirements.txt` file. After this you can run the Django server using the command `python manage.py runserver`.
This will create a database instance and then you can create a superuser to access the admin panel using the command `python manage.py createsuperuser`.

## Features

- Users can login and register to the library
- Users can view the list of available books in the library
- Users can loan books from the library (when logged in)
- Users can view a list of other users registered in the library
- Users can view a list of books they have loaned

## Future Improvements

- Improve UI/UX
- Redirection of users after logging in/loggin out
- Ability to return a book
- Add an admin panel to manage books and users (apart from Django admin)
- Time limit (expiration) on book loans
- Ability to request a book
- Deploy the app
