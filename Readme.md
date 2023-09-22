This project is intended to prototype a real business need and was build on a mac on the following required elements. The installation information is Mac OS X based, please adjust based on your operating system.

Python 3.11 *
Postgresql 14 *
Pip3 *
Flask 2.3.3
Flask-Migrate 4.0.4
Flask-SQLAlchemy 3.1.1
Jinja2 3.1.2
Psychopg2 2.9.7

* install with brew, the rest can be done with pip3

the following are non required elements:

Postico 2.0.4 *

The project was powered by:

Caffeine, paper, Trello and of course supervision from my cats.

As well as downloading the project files from github please make sure all required elements are installed and do the following to see this project at work:

1. git clone the repository
    git@github.com:LidzDev/pet-cms.git
2. in the terminal:
    cd pet-cms
3. In the terminal in the application folder execute:
    flask run
2. Open a browser and open http://127.0.0.1:4999/
3. In the terminal start postgres with:
    brew services start postgresql@14
4. In the terminal create the database with:
    createdb pet_cms
5. Open app.py with a code editor and comment line 8 and uncomment line 7 and replace 'postgres:password' with your postgres username
6. In the terminal run:
    flask db init
    flask db migrate
    flask db upgrade
    flask seed

<!-- consider using the markdown syntax to proply highlight and format the readme, here is a cheatsheet to get you started https://www.markdownguide.org/cheat-sheet/ -->
