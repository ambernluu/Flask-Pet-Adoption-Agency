from flask import Flask, render_template, request, redirect, flash
from models import Pet, db, connect_db
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "penguinz!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def list_pets():
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)



@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Renders pet form (GET) or handles pet form submission (POST)"""
    form = AddPetForm()
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)

        db.session.add(new_pet)
        db.session.commit()
        flash(f"Created new pet")
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form=form)

# @app.route('/<int:id>/edit', methods=["GET", "POST"])
# def edit_pet(id):
#     pet = Pet.query.get_or_404(id)
#     form = EditPetForm(obj=pet)
#     if form.validate_on_submit():
#         pet.photo_url = form.photo_url.data
#         pet.notes = form.notes.data 
#         pet.available = form.available.data

#         db.session.commit()
#         flash(f"{pet.name} has been updated")
#         return redirect('/')
#     else:
#         render_template("edit_pet_form.html", form=form, pet=pet)
#         # return redirect('/')

@app.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_pet(id):
    """Edit pet."""

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect('/')

    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)