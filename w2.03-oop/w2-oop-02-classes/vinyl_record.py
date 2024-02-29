"""
Create a `VinylRecord class`. Its constructor
should accept a dictionary as input.

The class should have the following properties:
    - title
    - artist
    - release_year
    - genre
    - plays

Write a play_record instance method that prints a
message to the terminal and increments the `plays`
attribute.

Write a calculate_age instance method that calculates
the age of the record and returns it. The method
should also print the age to the terminal. Use the
`datetime` module for this method.
"""


class VinylRecord:
    """This class is a representation of a vinyl record."""

    def __init__(self, data):
        """Constructor method for the VinylRecord class."""

        self.title = data["title"]
        self.artist = data["artist"]
        self.release_year = data["release_year"]
        self.genre = data["genre"]
        self.plays = 0

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
print(still_bill)

still_bill.play_record()
still_bill.play_record()
still_bill.play_record()
still_bill.play_record()
still_bill.play_record()
print(still_bill.plays)

blizz = VinylRecord(blizzard_data)
blizz.play_record()
blizz.play_record()
blizz.play_record()
blizz.play_record()
blizz.play_record()
blizz.play_record()
blizz.play_record()
blizz.play_record()
blizz.play_record()
blizz.play_record()
blizz.play_record()
blizz.play_record()
blizz.play_record()
print(blizz.plays)

# VinylRecord.play_record() ERROR
