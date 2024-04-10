from .model import User
from flask_login import current_user, login_user, logout_user
from .forms import SignUpForm, SignInForm
from flask import Blueprint, flash, redirect, render_template, request, url_for
from boops.extensions import bcrypt, db, login_manager


bp = Blueprint("auth", __name__, url_prefix="/auth")

# Flask-Login settings
login_manager.login_view = "auth.sign_in"
login_manager.login_message = "Please sign in."
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    """User loader for Flask-Login."""

    return User.query.get(int(user_id))


@bp.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    """
    GET: Displays the register form template.
    POST: Processes the register form.
    """

    form = SignUpForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # get valid user input
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data

            # Check if user's email already exists
            user = User.query.filter_by(email=email).first()
            if user:
                flash("Duplicate email. Please log in.", "warning")
                return redirect(url_for("auth.sign_in"))

            # hash password
            hashed_pw = bcrypt.generate_password_hash(password)

            # create User object and save to db
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=hashed_pw,
            )
            db.session.add(new_user)
            db.session.commit()

            # redirect user to sign-in page
            flash("Registration successful. Please log in.", "success")
            return redirect(url_for("auth.sign_in"))

    context = {"form": form, "current_user": current_user}
    return render_template("/auth/sign-up.html", **context)


@bp.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    """
    GET: Displays the login form template.
    POST: Processes the login form.
    """

    form = SignInForm()
    if form.validate_on_submit():
        # Get valid user input
        email = form.email.data
        password = form.password.data

        # Check if user's email exists and password is correct
        user: User = User.query.filter_by(email=email).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            flash("Invalid credentials.", "danger")
            return redirect(url_for("auth.sign_in"))

        # Log in the user
        login_user(user)
        return redirect(url_for("pets.pets"))

    context = {"form": form, "current_user": current_user}
    return render_template("/auth/sign-in.html", **context)


@bp.post("/sign-out")
def sign_out():
    logout_user()
    return redirect(url_for("main.index"))
