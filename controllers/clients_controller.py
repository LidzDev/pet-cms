from flask import Blueprint, render_template
from models.client import Client
from app import db

clients_blueprint = Blueprint("clients", __name__)

@clients_blueprint.route("/clients")
def list_clients():
    clients = Client.query.all()
    return render_template("clients/index.jinja", title = "My Pet Client Management System", clients = clients)