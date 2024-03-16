from flask_app import app

# import controllers here
# from flask_app.controllers import gizmos

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5500)
