from app import db
# from datetime import datetime

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    accepted = db.Column(db.Boolean)
    performed = db.Column(db.Boolean)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))


    def __repr__(self):
        return f"<Booking {self.id}: {self.date}>"