# Pet CMS

## Summary
Petsitter client CMS + visit booking page for clients

## Description
This project is intended to prototype a real business need and was build in python and flask and postgreSQL.   The installation information is Mac OS X based, please adjust based on your operating system.

## Dependencies
- Python 3.11 
- Postgresql 14 
- Pip3 

## Installing the dependencies
in your terminalb run the following:
```
brew install postgresql@14
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install flask-migrate
pip3 install python-dotenv
pip3 install psychopg2
```

## Running the project for the first time
1. [Pet CMS github](https://github.com/LidzDev/pet-cms/)
2. in the terminal run
   ```
   git clone git@github.com:LidzDev/pet-cms.git
   cd pet-cms
   flask run
   brew services start postgresql@14
   createdb pet_cms
   ```
3. Open app.py with a code editor and comment line 8 and uncomment line 7 and replace 'postgres:password' with your postgres username
4. In the terminal run:
 ```
    flask db init
    flask db migrate
    flask db upgrade
    flask seed
   ```
5. Open [PetCMS](http://127.0.0.1:4999/)
  
### The project was powered by:

Caffeine, paper, Trello and of course supervision from my cats.
