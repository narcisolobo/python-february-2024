class VinylRecord:
    """This class is a representation of a vinyl record."""

    num_records_created = 0  # class attribute

    def __init__(self, data):
        """Constructor method for the VinylRecord class."""

        self.title = data["title"]
        self.artist = data["artist"]
        self.release_year = data["release_year"]
        self.genre = data["genre"]
        self.plays = 0
        VinylRecord.num_records_created += 1
        self.owner = None

    @classmethod
    def reset_total_records(cls):
        """This resets num_records_created to zero."""

        cls.num_records_created = 0
        # VinylRecord.num_records_created = 0 alternate version

    @staticmethod
    def get_decade(year):
        """This method returns the decade of a given year."""

        return year - (year % 10)

    def play_record(self):
        """This method plays a record and increment its plays attribute by 1."""

        print(f"Playing {self.title}.")
        self.plays += 1
