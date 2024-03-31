import requests
from marvel.utilities import get_url, TLSAdapter
from flask import Blueprint, flash, redirect, render_template, request, session

bp = Blueprint("main", __name__)
search = {}


@bp.route("/", methods=["GET", "POST"])
def index():
    """This route renders the home page."""

    if "results" not in search:
        search["results"] = None

    if request.method == "POST":
        if len(request.form["search"].strip()) == 0:
            flash("Please enter search term.")
            return redirect("/")

        search_term = request.form["search"]
        url = get_url(search_term)
        print(search_term.center(50, "*"))

        requests_session = requests.session()
        requests_session.mount("https://", TLSAdapter())
        response = requests_session.get(url)
        json = response.json()
        search["results"] = json["data"]["results"]

        return redirect("/")

    return render_template("index.html", results=search.get("results"))
