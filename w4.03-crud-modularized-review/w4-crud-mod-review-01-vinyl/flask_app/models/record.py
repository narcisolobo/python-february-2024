from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


class Record:
    _db = "records_db"

    # this constructor accepts a dictionary as input
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.artist = data["artist"]
        self.genre = data["genre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    """
    CREATE A CLASS METHOD FOR EACH CRUD QUERY
    """

    @classmethod
    def find_all(cls):
        """Find all records in the database."""

        query = "SELECT * FROM records;"
        list_of_dicts = connectToMySQL(Record._db).query_db(query)
        pprint(list_of_dicts)

        records = []
        for each_dict in list_of_dicts:
            record = Record(each_dict)
            records.append(record)
        return records

    @classmethod
    def create(cls, form_data):
        """Inserts a new record into the database."""

        query = """
        INSERT INTO records
        (title, artist, genre)
        VALUES
        (%(title)s, %(artist)s, %(genre)s);
        """
        record_id = connectToMySQL(Record._db).query_db(query, form_data)
        return record_id

    @classmethod
    def find_by_id(cls, record_id):
        """Finds one record by id in the database."""

        query = "SELECT * FROM records WHERE id = %(record_id)s;"
        data = {"record_id": record_id}
        list_of_dicts = connectToMySQL(Record._db).query_db(query, data)
        print("***************************")
        pprint(list_of_dicts)
        print("***************************")
        # error handling
        if len(list_of_dicts) == 0:
            return None
        record = Record(list_of_dicts[0])
        return record

    @classmethod
    def update(cls, form_data):
        """Updates a record from a form."""

        query = """
        UPDATE records
        SET
        title=%(title)s,
        artist=%(artist)s,
        genre=%(genre)s
        WHERE id = %(record_id)s;
        """
        connectToMySQL(Record._db).query_db(query, form_data)
        return

    @classmethod
    def delete_by_id(cls, record_id):
        """Deletes a record by id."""

        query = "DELETE FROM records WHERE id = %(record_id)s;"
        data = {"record_id": record_id}
        connectToMySQL(Record._db).query_db(query, data)
        return
