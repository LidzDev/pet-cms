from flask import Blueprint, render_template, request, redirect
from models.pet import Pet
from models.client import Client
from app import db

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def list_pets():
    pets = Pet.query.all()
    return render_template("pets/index.jinja", title = "My Pet Client Management System", pets = pets)

@pets_blueprint.route("/pets/client/<int:id>")
def show_client_pets(id):
    client_to_show = Client.query.get(id)
    return render_template("pets/client.jinja", title=f"Hi {client_to_show.first_name}", client=client_to_show)

@pets_blueprint.route("/pets/client/add/<int:id>", methods=["POST"])
def save_client_pet(id):
    # print("anything happening here????")
    pet_name = request.form["pet_name"]
    pet_age = request.form["pet_age"]
    pet_to_save = Pet(pet_name=pet_name, age=pet_age, client_id=id)
    db.session.add(pet_to_save)
    db.session.commit()
    redirect_string = "/pets/client/" + str(id)
    return redirect(redirect_string)

@pets_blueprint.route("/pets/update/<int:id>", methods=["POST"])
def update_pet(id):
    pet = Pet.query.get(id)
    pet.pet_name = request.form["pet_name"]
    pet.age = request.form["pet_age"]
    db.session.commit()
    referrer = request.referrer
    return redirect(referrer)