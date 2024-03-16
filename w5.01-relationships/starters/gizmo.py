from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


class Gizmo:
    _db = "gizmos_db"

    def __init__(self, data):
        self.id = data["id"]
        self.column1 = data["column1"]
        self.column2 = data["column2"]
        self.column3 = data["column3"]
        self.column4 = data["column4"]
        self.column5 = data["column5"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def find_all(cls):
        """Finds all gizmos in the database."""

        query = "SELECT * FROM gizmos;"
        list_of_dicts = connectToMySQL(Gizmo._db).query_db(query)

        print("*************ALL GIZMOS**************")
        pprint(list_of_dicts)
        print("*************ALL GIZMOS**************")

        gizmos = []
        for each_dict in list_of_dicts:
            gizmo = Gizmo(each_dict)
            gizmos.append(gizmo)
        return gizmos

    @classmethod
    def find_by_id(cls, gizmo_id):
        """Finds one gizmo by id in the database."""

        query = "SELECT * FROM gizmos WHERE id = %(gizmo_id)s;"
        data = {"gizmo_id": gizmo_id}
        list_of_dicts = connectToMySQL(Gizmo._db).query_db(query, data)

        gizmo = Gizmo(list_of_dicts[0])
        return gizmo

    @classmethod
    def create(cls, form_data):
        """Creates a new gizmo from a form."""

        query = """
        INSERT INTO gizmos
        (column1, column2, column3, column4, column5)
        VALUES
        (%(column1)s, %(column2)s, %(column3)s, %(column4)s, %(column5)s);
        """
        gizmo_id = connectToMySQL(Gizmo._db).query_db(query, form_data)
        return gizmo_id

    @classmethod
    def update(cls, form_data):
        """Updates a gizmo from a form."""

        query = """
        UPDATE gizmos
        SET
        column1=%(column1)s,
        column2=%(column2)s,
        column3=%(column3)s,
        column4=%(column4)s,
        column5=%(column5)s
        WHERE id = %(gizmo_id)s;
        """
        connectToMySQL(Gizmo._db).query_db(query, form_data)
        return

    @classmethod
    def delete_by_id(cls, gizmo_id):
        """Deletes a gizmo by id."""

        query = "DELETE FROM gizmos WHERE id = %(gizmo_id)s;"
        data = {"gizmo_id": gizmo_id}
        connectToMySQL(Gizmo._db).query_db(query, data)
        return
