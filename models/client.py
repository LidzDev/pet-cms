from app import db

class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(255))
    street = db.Column(db.String(255))
    postcode = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    access_instructions = db.Column(db.Text)
    pets = db.relationship('Pet', backref='client')
    bookings = db.relationship('Booking', backref='client')

    def __repr__(self):
        return f'<Client {self.id}: {self.first_name} {self.last_name}>'