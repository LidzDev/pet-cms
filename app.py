from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/pet_cms" 
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://Lydia@localhost:5432/pet_cms"
# app.config["SQLALCHEMY_ECHO"]= True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models.client import Client
from models.pet import Pet
from models.booking import Booking

@app.route('/')
def home():
    return render_template('visual.jinja')