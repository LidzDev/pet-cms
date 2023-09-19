from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/pet_cms" 
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lydia@localhost:5432/pet_cms"
app.config["SQLALCHEMY_ECHO"]= False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from seed import seed
app.cli.add_command(seed)

from controllers.clients_controller import clients_blueprint
from controllers.bookings_controller import bookings_blueprint

app.register_blueprint(clients_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    return render_template('visual.jinja', title ="Hello World")

if __name__ == '__main__':
    app.run(debug=True)