from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", y=8, x=8, color0="black", color1="red")


@app.route("/play/<int:y>")
def play_y(y):
    return render_template("index.html", y=y, x=8, color0="black", color1="red")


@app.route("/play/<int:y>/<int:x>")
def play_y_x(y, x):
    return render_template("index.html", y=y, x=x, color0="black", color1="red")


@app.route("/play/<int:y>/<int:x>/<color0>/<color1>")
def play_y_x_color(y, x, color0, color1):
    return render_template("index.html", y=y, x=x, color0=color0, color1=color1)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5500)
