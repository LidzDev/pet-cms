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

@bookings_blueprint.route("/bookings/add/<int:id>", methods=["POST"])
def save_client_booking(id):
    # print("anything happening here????")
    booking_date = request.form["booking_date"]
    # print(booking_date)
    booking_to_insert = Booking(date=booking_date, client_id=id)
    db.session.add(booking_to_insert)
    db.session.commit()
    redirect_string = "/bookings/client/" + str(id)
    return redirect(redirect_string)