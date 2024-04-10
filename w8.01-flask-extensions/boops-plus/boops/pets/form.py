from datetime import date
from flask_wtf import FlaskForm
from wtforms import DateField, RadioField, StringField, ValidationError
from wtforms.validators import AnyOf, InputRequired, Length


class PetForm(FlaskForm):
    """The pet form class."""

    name = StringField(
        "Name:",
        validators=[
            InputRequired("Please enter your pet's name."),
            Length(min=2, max=45, message="Name must be between 2 and 45 characters."),
        ],
    )
    type = StringField(
        "Type:",
        validators=[
            InputRequired("Please enter your pet's type."),
            Length(min=2, max=45, message="Type must be between 2 and 45 characters."),
        ],
    )
    birthday = DateField(
        "Birthday:", validators=[InputRequired("Please enter your pet's birthday.")]
    )
    is_derpy = RadioField(
        "Is your pet derpy?",
        choices=[(0, "No"), (1, "Yes")],
        coerce=int,
        validators=[
            InputRequired("Please choose yes or no."),
            AnyOf([0, 1], message="Invalid input."),
        ],
    )

    def validate_birthday(form, field: DateField):
        today = date.today()
        if field.data > today:
            raise ValidationError("Birthday must be in the past.")
