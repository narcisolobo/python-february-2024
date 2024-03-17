from flask_app.config.mysqlconnection import connectToMySQL


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
