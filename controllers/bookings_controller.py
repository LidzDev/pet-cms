from flask import Blueprint, render_template, request, redirect
from models.booking import Booking
from models.client import Client
from app import db

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def list_bookings():
    bookings = Booking.query.all()
    return render_template("bookings/index.jinja", title = "My Pet Client Management System", bookings = bookings)

@bookings_blueprint.route("/bookings/client/<int:id>")
def show_client_booking(id):
    client_to_show = Client.query.get(id)
    return render_template("bookings/client.jinja", title=f"Hi {client_to_show.first_name}", client=client_to_show)

# @clients_blueprint.route("/clients/<int:id>", methods=["POST"])
# def update_client(id):
#     client = Client.query.get(id)
#     client.first_name = request.form["first_name"]
#     client.last_name = request.form["last_name"]
#     client.email = request.form["email"]
#     client.phone = request.form["phone"]
#     client.street = request.form["street"]
#     client.postcode = request.form["postcode"]
#     db.session.commit()
#     redirect_string = "/clients/" + str(id)
#     return redirect(redirect_string)

# @clients_blueprint.route("/clients/add")
# def show_add_client():
#     return render_template("clients/add.jinja", title="Add a new Client to the CMS")

# @clients_blueprint.route("/clients/add", methods=["POST"])
# def save_client():
#     first_name = request.form["first_name"]
#     last_name = request.form["last_name"]
#     email = request.form["email"]
#     phone = request.form["phone"]
#     street = request.form["street"]
#     postcode = request.form["postcode"]
#     client_to_be_saved = Client(first_name=first_name, last_name=last_name, email=email, phone=phone, street=street, postcode=postcode)
#     db.session.add(client_to_be_saved)
#     db.session.commit()
#     return redirect("/clients")

# @clients_blueprint.route("/clients/delete/<int:id>", methods=["POST"])
# def delete_client(id):
#     client = Client.query.get(id)
#     db.session.delete(client)
#     db.session.commit()
#     return redirect("/clients")