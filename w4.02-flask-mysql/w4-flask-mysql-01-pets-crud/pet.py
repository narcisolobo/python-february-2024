from mysqlconnection import connectToMySQL
from pprint import pprint


class Pet:
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
        list_of_dicts = connectToMySQL("pets_db").query_db(query)
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
        pet_id = connectToMySQL("pets_db").query_db(query, form_data)
        return pet_id
