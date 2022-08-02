from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

species_options = ["Cat", "Dog", "Porcupine"]

class AddPetForm(FlaskForm):
    name = StringField("Animal Name",  validators=[
                       InputRequired(message="Animal Name can't be blank")])
    species = SelectField('State', choices=[(sp, sp) for sp in species_options])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[
                       Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Notes",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")