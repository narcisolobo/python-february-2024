"""
=== === FUNCTIONS EXERCISE === ===
Write a Python program that defines a function called `calculate_average` to calculate the average of a list of numbers. The program should take a list of numbers as input from the user and then call the `calculate_average` function to compute the average. Finally, it should print the average.

Example Output:

Enter the numbers separated by spaces: 10 20 30 40 50
The average is: 30.0
"""


def app():
    """
    This function is our entry-point. It calls all the
    other functions and prints the result.
    """
    num_string = prompt()
    num_int_list = split_string_into_list_of_ints(num_string)
    average = calculate_average(num_int_list)
    print(f"The average is: {average}")


def prompt():
    """
    This function prompts the user for numbers
    separated by commas and returns it.
    """
    print("Enter the numbers separated by spaces.")
    num_string = input()
    return num_string


def split_string_into_list_of_ints(string_with_spaces):
    """
    This function splits a string into a list at
    every space, converts each element into an
    integer, and returns the list.
    """
    num_string_list = string_with_spaces.split(" ")
    num_int_list = []
    for num_string in num_string_list:
        num_int_list.append(int(num_string))
    return num_int_list


def calculate_average(num_int_list):
    """
    This function takes in a list of integers and
    returns their average.
    """
    sum = 0
    for num in num_int_list:
        sum = sum + num
    average = sum / len(num_int_list)
    return average


# Down here, we call the app function to start the app
app()
