from app import db

def handle_delete_client(client):
    for pet in client.pets: 
        db.session.delete(pet)
    for booking in client.bookings:
        db.session.delete(booking)
    db.session.delete(client)
    db.session.commit()