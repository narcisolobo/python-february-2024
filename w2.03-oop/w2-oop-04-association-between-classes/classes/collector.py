from classes.vinyl_record import VinylRecord
from typing import List


class Collector:
    def __init__(self, name):
        self.name = name
        self.collection: List[VinylRecord] = []

    def add_record(self, record):
        # add a record to the collection
        # assign an owner to the record
        self.collection.append(record)
        record.owner = self
