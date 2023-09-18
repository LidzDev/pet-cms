from flask import Blueprint, render_template
from models.client import Client
from app import db

clients_blueprint = Blueprint("clients", __name__)

@clients_blueprint.route("/clients")
def list_clients():
    clients = Client.query.all()
    return render_template("clients/index.jinja", title = "My Pet Client Management System", clients = clients)

@clients_blueprint.route("/clients/<int:id>")
def show_one_client(id):
    client_to_show = Client.query.get(id)
    return render_template("clients/show.jinja", title=f"Pet CMS Client: {client_to_show.first_name} {client_to_show.last_name}", client=client_to_show)