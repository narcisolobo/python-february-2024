class SuperMarket:
    """This class defines a SuperMarket object."""

    def __init__(self, type, name, location):
        """The SuperMarket constructor method."""

        self.type = type
        self.name = name
        self.location = location
        self.is_open = False

    def __str__(self):
        return f"<SuperMarket object: {self.name}>"

    # instance method
    def display_info(self):
        """This method prints all attributes of a supermarket instance/object."""

        print(
            f"Type: {self.type}, Name: {self.name}, Location: {self.location}, Open? {self.is_open}"
        )
        return self  # facilitates chaining methods

    def open_supermarket(self):
        """This method opens a store."""

        if not self.is_open:
            self.is_open = True
            print(f"The {self.name} is now open.")
        else:
            print(f"The {self.name} is already open.")

        return self  # facilitates chaining methods


dojoMarket = SuperMarket("budget", "Dojo Market", "Seattle")

dojoMarket.display_info().open_supermarket()
dojoMarket.open_supermarket().display_info()

print(dojoMarket)

# Four Pillars of OOP
"APIE"

"""
Abstraction
Polymorphism
Inheritance
Encapsulation
"""
