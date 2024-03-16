from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


class Pet:
    _db = "pets_db"

    # this constructor accepts a dictionary as input
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.type = data["type"]
        self.birthday = data["birthday"]
        self.is_derpy = data["is_derpy"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    """
    CREATE A CLASS METHOD FOR EACH CRUD QUERY
    """

    @classmethod
    def find_all(cls):
        """Find all pets in the database."""

        query = "SELECT * FROM pets;"
        list_of_dicts = connectToMySQL(Pet._db).query_db(query)
        pprint(list_of_dicts)

        pets = []
        for each_dict in list_of_dicts:
            pet = Pet(each_dict)
            pets.append(pet)
        return pets

    @classmethod
    def create(cls, form_data):
        """Inserts a new pet into the database."""

        query = """
        INSERT INTO pets
        (name, type, birthday, is_derpy)
        VALUES
        (%(name)s, %(type)s, %(birthday)s, %(is_derpy)s);
        """
        pet_id = connectToMySQL(Pet._db).query_db(query, form_data)
        return pet_id

    @classmethod
    def find_by_id(cls, pet_id):
        """Finds one pet by id in the database."""

        query = "SELECT * FROM pets WHERE id = %(pet_id)s;"
        data = {"pet_id": pet_id}
        list_of_dicts = connectToMySQL(Pet._db).query_db(query, data)
        print("***************************")
        pprint(list_of_dicts)
        print("***************************")
        # error handling
        if len(list_of_dicts) == 0:
            return None
        pet = Pet(list_of_dicts[0])
        return pet

    @classmethod
    def update(cls, form_data):
        """Updates a pet from a form."""

        query = """
        UPDATE pets
        SET
        name=%(name)s,
        type=%(type)s,
        birthday=%(birthday)s,
        is_derpy=%(is_derpy)s
        WHERE id = %(pet_id)s;
        """
        connectToMySQL(Pet._db).query_db(query, form_data)
        return

    @classmethod
    def delete_by_id(cls, pet_id):
        """Deletes a pet by id."""

        query = "DELETE FROM pets WHERE id = %(pet_id)s;"
        data = {"pet_id": pet_id}
        connectToMySQL(Pet._db).query_db(query, data)
        return
