from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional


class PetForm(FlaskForm):
    """Form to add a new pet to agency"""

    name = StringField("Name", validators=[
                       InputRequired(message='Name is required')])
    species = StringField("Species", validators=[InputRequired(
        message='Species of this pet is required')])
    photo_url = StringField("Photo of Pet", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional()])
    notes = IntegerField("Notes", validators=[Optional()])
    available = BooleanField("Available for Adoption")
