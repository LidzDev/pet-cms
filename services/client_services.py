from app import db
##########################
# example of extracting logic 
##########################


def handle_delete_client(client):
    for pet in client.pets: 
        db.session.delete(pet)
    for booking in client.bookings:
        db.session.delete(booking)
    db.session.delete(client)
    db.session.commit()

def get_redirect_string(referrer):
    if "/clients/me/" in referrer:
        return"/"
    else: 
        return "/clients"