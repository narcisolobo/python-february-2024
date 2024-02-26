# Class and Static Methods
Up to now we've been creating instance attributes and instance methods.

Instance attributes are unique to each instance of a class and are defined in the `__init__` constructor method.

Instance methods are methods that belong to an object of the class, rather than the class itself.

## Class Attributes and Class Methods
Class Attributes are shared among all instances of the class and are defined outside of any method in the class definition.

## Static Methods
Static methods are similar to class methods, the difference being that a static method is bound only to the class, while a class method is bound to the class and shared amongst all instances of that class.

This means that a static method can be called without an object for that class.

This also means that static methods cannot modify the state of an object as they are not bound to it.

## Code
Let's revisit our `Guitar` class and add class and static methods.

```py
class Guitar:
    # Class attribute
    num_guitars_in_stock = 0 

    def __init__(self, brand, model, num_strings = 6):
        self.brand = brand
        self.model = model
        self.num_strings = num_strings
        self.is_playing = False
        Guitar.num_guitars_in_stock += 1 # increment

    def start_playing(self):
        self.is_playing = True
        print(f"The {self.brand} {self.model} is now being played.")

    def stop_playing(self):
        self.is_playing = False
        print(f"The {self.brand} {self.model} has stopped playing.")

    @classmethod
    def display_stock(cls):
        print(f"Number of guitars in stock: {cls.num_guitars_in_stock}")

    @staticmethod
    def standard_tuning():
        print("E, A, D, G, B, E")


# Create instances of the Guitar class
guitar1 = Guitar("Fender", "Stratocaster", 6)
guitar2 = Guitar("Gibson", "Les Paul", 6)

# Access class attributes and call class methods
print(Guitar.num_guitars_in_stock)    # Output: 2
Guitar.display_stock()                # Output: Number of guitars in stock: 2

# Output: E, A, D, G, B, E
Guitar.standard_tuning()
```
