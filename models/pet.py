from app import db

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))


    def __repr__(self):
        return f"<Pet {self.id}: {self.pet_name}>"