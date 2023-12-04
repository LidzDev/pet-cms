# Pet CMS

## Summary
Petsitter client CMS + visit booking page for clients

## Description
This project is intended to prototype a real business need and was build in python and flask and postgreSQL.   The installation information is Mac OS X based, please adjust based on your operating system.

## Dependencies
- Python 3.11 
- Postgresql 14 
- Pip3 

## Installation 
run the following:
```
brew install postgresql@14
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install flask-migrate
pip3 install python-dotenv
pip3 install psychopg2
```

## Running the project
1. git clone the repository
    git@github.com:LidzDev/pet-cms.git
2. in the terminal run
   ```
   cd pet-cms
   flask run
   brew services start postgresql@14
   createdb pet_cms
   ```
3. Open a browser and open http://127.0.0.1:4999/
4. Open app.py with a code editor and comment line 8 and uncomment line 7 and replace 'postgres:password' with your postgres username
5. In the terminal run:
 ```
    flask db init
    flask db migrate
    flask db upgrade
    flask seed
   ```
### The project was powered by:

Caffeine, paper, Trello and of course supervision from my cats.
