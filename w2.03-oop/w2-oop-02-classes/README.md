# Classes
To create a class in Python, you use the `class` keyword followed by the name of the class. Here's the basic syntax for creating a class:

```py
class ClassName:
    # Class attributes and methods
    pass
```
Let's break down the components of a class:
- `class`: The `class` keyword is used to indicate the start of a class definition.
- `ClassName`: This is the name of the class. It should follow Python's naming conventions, which typically use PascalCase (each word capitalized without underscores).
- `pass`: The `pass` keyword is a placeholder that allows an empty class definition. You can replace it with class attributes and methods.

Here's an example of a simple class called `Guitar` with some attributes and methods:

```py
class Guitar:
    def __init__(self, brand, model, num_strings):
        self.brand = brand
        self.model = model
        self.num_strings = num_strings
        self.is_playing = False

    def play(self):
        self.is_playing = True
        print(f"The {self.brand} {self.model} is now being played.")

    def stop_playing(self):
        self.is_playing = False
        print(f"The {self.brand} {self.model} has stopped playing.")

    def tune(self):
        print(f"Tuning the {self.brand} {self.model}.")

    def change_strings(self, new_num_strings):
        self.num_strings = new_num_strings
        print(f"The {self.brand} {self.model} now has {self.num_strings} strings.")



```
In this example, the `Guitar` class has the following components:

- **Initializer or constructor ("dunder init"):** The __init__ method is a special method that is called when creating a new instance of the class. It initializes the instance with the provided attributes.
- **Attributes:**
  - `brand`: The brand of the guitar.
  - `model`: The model of the guitar.
  - `num_strings`: The number of strings on the guitar.
  - `is_playing`: A boolean attribute to represent whether the guitar is currently being played or not.
- **Instance methods:** Instance methods operate on an instance of the class. They take the `self` parameter, which refers to the current instance, and can access and modify instance attributes.
  - `play(self)`: Sets the is_playing attribute to True and prints a message indicating that the guitar is being played.
  - `stop_playing(self)`: Sets the is_playing attribute to False and prints a message indicating that the guitar has stopped playing.
  - `tune(self)`: Prints a message indicating that the guitar is being tuned.
  - `change_strings(self, new_num_strings)`: Updates the num_strings attribute with the provided value and prints a message indicating the new number of strings.

Once the class is defined, we can create instances (objects) of the class by calling the class name as if it were a function. We can then access the attributes and call the methods on each guitar instance.

```py
# Create instances of the Guitar class
guitar1 = Guitar("Fender", "Stratocaster", 6)
guitar2 = Guitar("Gibson", "Les Paul", 6)

# Access attributes and call methods on the guitar instances
print(guitar1.brand)                  # Output: Fender
print(guitar2.model)                  # Output: Les Paul

guitar1.play()                        # Output: The Fender Stratocaster is now being played.
guitar2.stop_playing()                # Output: The Gibson Les Paul has stopped playing.

guitar1.tune()                        # Output: Tuning the Fender Stratocaster.
guitar2.change_strings(12)            # Output: The Gibson Les Paul now has 12 strings.
```