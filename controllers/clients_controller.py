from flask import Blueprint, render_template, request, redirect
from models.client import Client
from models.pet import Pet
from models.booking import Booking
from app import db
from helpers.data import handle_delete_client

clients_blueprint = Blueprint("clients", __name__)

@clients_blueprint.route("/clients")
def list_clients():
    clients = Client.query.all()
    return render_template("clients/index.jinja", title = "My Pet Client Management System", clients = clients)

@clients_blueprint.route("/clients/<int:id>")
def show_one_client(id):
    client_to_show = Client.query.get(id)
    return render_template("clients/show.jinja", title=f"Pet CMS Client: {client_to_show.first_name} {client_to_show.last_name}", client=client_to_show)

@clients_blueprint.route("/clients/me/<int:id>")
def show_my_client_detail(id):
    client_to_show = Client.query.get(id)
    return render_template("clients/me.jinja", title=f"Hi {client_to_show.first_name}", client=client_to_show)

@clients_blueprint.route("/clients/<int:id>", methods=["POST"])
def update_client(id):
    client = Client.query.get(id)
    client.first_name = request.form["first_name"]
    client.last_name = request.form["last_name"]
    client.email = request.form["email"]
    client.phone = request.form["phone"]
    client.street = request.form["street"]
    client.postcode = request.form["postcode"]
    db.session.commit()
    referrer = request.referrer
    print(f"the referrer is {referrer}")
    if "/clients/me/" in referrer:
        redirect_string = "/clients/me/" + str(id)
    else: 
        redirect_string = "/clients/" + str(id)
    print(f"the redirect is {redirect_string}")
    return redirect(redirect_string)

@clients_blueprint.route("/clients/update_special/<int:id>", methods=["POST"])
def update_special(id):
    client = Client.query.get(id)
    client.access_instructions = request.form["access_instructions"]
    db.session.commit()
    referrer = request.referrer
    if "127.0.0" in referrer:
        return redirect(referrer)
    else: return("error!!!!!")

@clients_blueprint.route("/clients/add")
def show_add_client():
    return render_template("clients/add.jinja", title="Add a new Client to the CMS")

@clients_blueprint.route("/clients/add", methods=["POST"])
def save_client():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]
    street = request.form["street"]
    postcode = request.form["postcode"]
    client_to_be_saved = Client(first_name=first_name, last_name=last_name, email=email, phone=phone, street=street, postcode=postcode)
    db.session.add(client_to_be_saved)
    db.session.commit()
    return redirect("/clients")

@clients_blueprint.route("/clients/delete/<int:id>", methods=["POST"])
def delete_client(id):
    client = Client.query.get(id)
    handle_delete_client(client)
    referrer = request.referrer
    if "/clients/me/" in referrer:
        redirect_string = "/"
    else: 
        redirect_string = "/clients"
    print(f"the redirect is {redirect_string}")
    return redirect(redirect_string)
