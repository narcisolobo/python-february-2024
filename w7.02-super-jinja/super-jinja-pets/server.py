from flask_app import app

# Remember to import your controllers here
from flask_app.controllers import pets

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5500)
