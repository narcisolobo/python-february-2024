"""
Using the `VinylRecord class`, create a class
attribute that tracks how many records have been
created.

Revise the existing instance method to accommodate
method chaining. We should be able to chain the
`play_record` method like so:

still_bill.play_record().play_record()

Write a reset_total_records class method that
prints a short message to the terminal and resets
the total record count to zero.

Write a get_decade static method to convert a release
year to the corresponding decade.

VinylRecord.get_decade(still_bill.release_year)
# prints "1970"
"""


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


still_bill_data = {
    "artist": "Bill Withers",
    "release_year": 1972,
    "title": "Still Bill",
    "genre": "Funk",
}

blizzard_data = {
    "title": "Blizzard of Ozz",
    "genre": "Metal",
    "artist": "Ozzy Osbourne",
    "release_year": 1980,
}

still_bill = VinylRecord(still_bill_data)
blizzard = VinylRecord(blizzard_data)

print(VinylRecord.num_records_created)
VinylRecord.reset_total_records()
print(VinylRecord.num_records_created)

print(VinylRecord.get_decade(still_bill.release_year))
print(VinylRecord.get_decade(blizzard.release_year))
