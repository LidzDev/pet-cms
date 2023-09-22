from flask import Blueprint, render_template, request, redirect
from models.client import Client
from models.pet import Pet
from models.booking import Booking
from services.client_services import get_redirect_string, handle_delete_client
from app import db

# we can consider extracting out logic and extra verbosity from our controller functions into a separate file, we care more about _what_ are code is doing as opposed to _how_ its doing it. 
# see below for example
# this has the following benefits ..

# 1. Separation of concerns
# One of the core principles of software engineering is the separation of concerns. By moving business logic out of controllers and into separate components, you ensure that each component has a single responsibility. Controllers should primarily handle user input and orchestrate the flow of data, while logic related to data manipulation, validation, and business rules should be handled by other parts of the application.
# 2. Code Reusability (keeps us DRY)
# Extracting logic into separate modules or classes makes it more reusable. You can use the same logic in multiple controllers or even in different parts of your application. This reduces code duplication and leads to a more maintainable codebase.
# 3. Scalable 
# As your application grows, you may need to change or extend its functionality, if we have to do the same action several times, it helps if we have the logic to do that action central to one place if we suddenly need to change how we are doing that action we now need to just change the code in one place as apposed to every place we where doing that action.
# 4. Readability 
# Controllers are typically responsible for managing the flow of requests and responses. When logic is mixed with controller code, it can make controllers bulky and less readable. Extracting logic into separate files/folders leads to cleaner, more focused, and more readable code. This improves the overall maintainability of the application. 

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
        redirect_string = "/clients/me/" + str(id) #redundent use of str() as <int:id> in the controller route already sets it to be a int
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
    for pet in client.pets: 
        pet = Pet.query.get(pet.id)# redudent request to db, we already have each pet associated with our client. as the '.pets' property is a list of pet objects
        db.session.delete(pet)
    for booking in client.bookings:
        booking = Booking.query.get(booking.id)
        db.session.delete(booking)
    db.session.delete(client)
    db.session.commit()
    referrer = request.referrer
    if "/clients/me/" in referrer:
        redirect_string = "/"
    else: 
        redirect_string = "/clients"
    print(f"the redirect is {redirect_string}")
    return redirect(redirect_string)

##########################
# example of extracting logic 
##########################

# @clients_blueprint.route("/clients/delete/<int:id>", methods=["POST"])
# def delete_client(id):
#     client = Client.query.get(id)

#     handle_delete_client(client)
#     redirect_string = get_redirect_string(request.referrer)

#     return redirect(redirect_string)

# this leaves us with code that reads more like natural language, making it easier to interpret, it also means if we have to add more cases to our redirect string, we won't have to create a long chain of elif's in our controller.