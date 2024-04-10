from re import compile
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import Email, EqualTo, InputRequired, Length, Regexp

PASSWORD_REGEX = compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$")


class SignUpForm(FlaskForm):
    """The sign up form class."""

    first_name = StringField(
        "First name:",
        validators=[
            InputRequired("Please enter your first name."),
            Length(
                min=2, max=45, message="First name must be between 2 and 45 characters."
            ),
        ],
    )
    last_name = StringField(
        "Last name:",
        validators=[
            InputRequired("Please enter your last name."),
            Length(
                min=2, max=45, message="Last name must be between 2 and 45 characters."
            ),
        ],
    )
    email = EmailField(
        "Email:",
        validators=[InputRequired("Please enter your email."), Email("Invalid email.")],
    )
    password = PasswordField(
        "Password:",
        validators=[
            InputRequired("Please enter your password."),
            Regexp(
                PASSWORD_REGEX,
                message="At least 8 characters, 1 upper, 1 lower, 1 number.",
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm password:",
        validators=[
            InputRequired("Please re-type your password."),
            EqualTo("password", message="Passwords do not match."),
        ],
    )


class SignInForm(FlaskForm):
    """The sign in form class."""

    email = EmailField(
        "Email:",
        validators=[InputRequired("Please enter your email."), Email("Invalid email.")],
    )
    password = PasswordField(
        "Password:",
        validators=[
            InputRequired("Please enter your password."),
            Regexp(
                PASSWORD_REGEX,
                message="At least 8 characters, 1 upper, 1 lower, 1 number.",
            ),
        ],
    )
