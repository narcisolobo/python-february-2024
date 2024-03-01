# Create a Hero class with appropriate properties.
# The constructor method should accept a dictionary
# as input.

# Create a display_info instance method that prints each
# attribute.

# Create a class method `get_heroes(cls, list_of_dicts)`
# that populates and returns a list of Hero objects.
# It should accept a list of dictionaries as input.


class Hero:
    def __init__(self, data):
        self.name = data["name"]
        self.hero_name = data["hero_name"]
        self.kanji_name = data["kanji_name"]
        self.quirk = data["quirk"]

    def display_info(self):
        print(
            f"""
                Name: {self.name}
                Hero name: {self.hero_name}
                Kanji name: {self.kanji_name}
                Quirk: {self.quirk}
            """
        )

    @classmethod
    def get_heroes(cls, list_of_dicts):
        """This class method populates and returns a list of Hero objects."""

        hero_objects = []
        for each_dict in list_of_dicts:
            hero_objects.append(Hero(each_dict))
        return hero_objects
