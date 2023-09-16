from app import db

from models.client import Client
from models.pet import Pet
from models.booking import Booking
from datetime import datetime
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext

def seed():

    print("start seed")
    Pet.query.delete()
    Booking.query.delete()
    Client.query.delete()
    client1 = Client(first_name = "Tim", last_name = "Henman",  email = "Tim.henman@domain.com", street = "20 Wimbledon Avenue" , postcode = "EH1 AAA", phone = "01234 567890")
    client2 = Client(first_name = "Jamie", last_name = "Henman",  email = "Jamie.henman@domain.com", street = "40 Wimbledon Avenue" , postcode = "EH1 AAB", phone = "01234 567891")
    client3 = Client(first_name = "Martha", last_name = "Henman",  email = "Martha.henman@domain.com", street = "11 Augusta Street" , postcode = "EH111 ZZZ", phone = "01234 568891")

    pet1 = Pet(pet_name = "Harley", age = 3, client_id = 1)
    pet2 = Pet(pet_name = "Shadow", age = 10, client_id = 2)
    pet3 = Pet(pet_name = "Copper", age = 7, client_id = 3)
    pet4 = Pet(pet_name = "Tiramisu", age = 2, client_id = 3)

    date1 = datetime(2022, 4, 30)
    date2 = datetime(2022, 7, 29)
    date3 = datetime(2023, 8, 1)
    date4 = datetime(2023, 9, 5)

    booking1 = Booking(date=date1, client_id = 1)
    booking2 = Booking(date=date2, client_id = 2)
    booking3 = Booking(date=date3, client_id = 3)
    booking4 = Booking(date=date4, client_id = 3)

    db.session.add(client1)
    db.session.add(client2)
    db.session.add(client3)

    db.session.add(pet1)
    db.session.add(pet2)
    db.session.add(pet3)
    db.session.add(pet4)

    db.session.add(booking1)
    db.session.add(booking2)
    db.session.add(booking3)
    db.session.add(booking4)

    db.session.commit()
    print("finished seeding")