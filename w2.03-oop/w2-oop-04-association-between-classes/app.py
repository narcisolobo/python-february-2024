from classes.collector import Collector
from classes.vinyl_record import VinylRecord

"""
Create a classes package. It should contain two
modules - vinyl_record and collector.

in collector, create a `Collector` class. The
constructor should accept a dictionary as input.

The class will have the following properties:
    - name
    - collection

The collection attribute's value will initially be
an empty list.

In vinyl_record, paste the `VinylRecord` class.
add a new attribute to the class - `owner`. Its
value will initially be `None`.

Back in the collector module, add a new instance
method - `add_record`. This method adds a `VinylRecord`
object to the `Collector` instance's `collection`
attribute and assigns the `Collector` instance to
the `VinylRecord` instance's `owner` attribute.

Test your code here in app.py.
"""

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

shane = Collector("Shane")
josé = Collector("José")

josé.add_record(blizzard)
josé.add_record(still_bill)

print(still_bill.owner.name)

for record in josé.collection:
    print(record.title)
