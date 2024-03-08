from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """This view returns a rendered index.html template."""

    return render_template(
        "index.html", new_heading="F String Baybeeehh!", body_color="aqua", num=1
    )


@app.route("/<new_heading>")
def new_heading(new_heading):
    """The view changes the default h1 content."""

    return render_template(
        "index.html", new_heading=new_heading, body_color="aqua", num=1
    )


@app.route("/<new_heading>/<body_color>")
def new_heading_body_color(new_heading, body_color):
    """The view changes the default h1 content and the body color."""

    return render_template(
        "index.html", new_heading=new_heading, body_color=body_color, num=1
    )


@app.route("/<new_heading>/<body_color>/<int:num>")
def new_heading_body_color_num(new_heading, body_color, num):
    """The view changes the default h1 content and the body color and the number of images."""

    return render_template(
        "index.html", new_heading=new_heading, body_color=body_color, num=num
    )


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
