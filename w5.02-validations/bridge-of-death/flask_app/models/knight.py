from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime


class Knight:
    _db = "bridge_of_death_db"

    def __init__(self, data):
        self.id = data["id"]
        self.username = data["username"]
        self.quest = data["quest"]
        self.birthday = data["birthday"]
        self.favorite_color = data["favorite_color"]
        self.is_afraid = data["is_afraid"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def form_is_valid(form_data):
        """This method validates the knight form."""

        is_valid = True

        if len(form_data["username"].strip()) == 0:
            is_valid = False
            flash("Please enter name.")
        elif len(form_data["username"].strip()) < 3:
            is_valid = False
            flash("Name must be at least three characters.")
        if len(form_data["quest"].strip()) == 0:
            is_valid = False
            flash("Please enter quest.")
        elif len(form_data["quest"].strip()) < 3:
            is_valid = False
            flash("Quest must be at least three characters.")
        if "favorite_color" not in form_data:
            is_valid = False
            flash("Please select color.")
        elif form_data["favorite_color"] not in ["blue", "yellow"]:
            is_valid = False
            flash("Invalid color chosen.")
        if len(form_data["birthday"].strip()) == 0:
            is_valid = False
            flash("Please enter birthday.")
        else:
            try:
                date_object = datetime.strptime(form_data["birthday"], "%m-%d-%Y")
                print(type(date_object))
            except:
                is_valid = False
                flash("Invalid birthday value.")
        if "is_afraid" not in form_data:
            is_valid = False
            flash("Please select scared option.")
        elif form_data["is_afraid"] not in ["0", "1"]:
            is_valid = False
            flash("Invalid scared option.")

        return is_valid

    @classmethod
    def create(cls, form_data):
        """Creates a new knight from a form."""

        query = """
        INSERT INTO knights
        (username, quest, birthday, favorite_color, is_afraid)
        VALUES
        (%(username)s, %(quest)s, %(birthday)s, %(favorite_color)s, %(is_afraid)s);
        """
        knight_id = connectToMySQL(Knight._db).query_db(query, form_data)
        return knight_id

    @classmethod
    def find_all(cls):
        """Finds all knights in the database."""

        query = "SELECT * FROM knights;"
        list_of_dicts = connectToMySQL(Knight._db).query_db(query)

        knights = []
        for each_dict in list_of_dicts:
            knight = Knight(each_dict)
            knights.append(knight)
        return knights

    @classmethod
    def find_by_id(cls, knight_id):
        """Finds one knight by id in the database."""

        query = "SELECT * FROM knights WHERE id = %(knight_id)s;"
        data = {"knight_id": knight_id}
        list_of_dicts = connectToMySQL(Knight._db).query_db(query, data)

        knight = Knight(list_of_dicts[0])
        return knight
