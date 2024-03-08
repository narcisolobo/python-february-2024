from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Render the index.html template."""

    return render_template("index.html")


@app.route("/services")
def services():
    """Render the services.html template."""

    message_variable = "These are our services."

    services_list = [
        {
            "name": "Website Development",
            "description": "We provide excellent website development.",
        },
        {
            "name": "Logo Creation",
            "description": "We provide excellent logo creation.",
        },
    ]

    is_available = False

    return render_template(
        "services.html",
        message_template=message_variable,
        services_list=services_list,
        is_available=is_available,
    )


@app.route("/about")
def about():
    """Render the about.html template."""

    return render_template("about.html")


@app.route("/contact")
def contact():
    """Render the contact.html template."""

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
