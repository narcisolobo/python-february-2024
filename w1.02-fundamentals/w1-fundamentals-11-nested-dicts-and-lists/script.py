from pprint import pprint

"""
=== === NESTED DICTIONARIES & LISTS === ===
Nesting is also allowed in dictionaries. In other words,
dictionaries may contain lists and tuples as well as other
dictionaries. Likewise, lists may contain dictionaries. All
of these may be many levels deep!
"""

monty_python = [
    {"first_name": "Graham", "last_name": "Chapman"},
    {"first_name": "John", "last_name": "Cleese"},
    {"first_name": "Terry", "last_name": "Gilliam"},
    {"first_name": "Eric", "last_name": "Idle"},
    {"first_name": "Terry", "last_name": "Jones"},
]

# Loop through the list of dictionaries with a nested for loop
# and the .items method
print("LOOK HERE BRO".center(50, "="))
for comedian in monty_python:
    output = ""
    for key, val in comedian.items():
        output += f"{key} - {val}, "
    print(output[:-2])
print("*****************")


# Add Michael Palin to the list.
monty_python.append({"first_name": "Michael", "last_name": "Palin"})
pprint(monty_python)

# Getting and Setting Values in Nested Dictionaries
# Print "Gilliam".

print(monty_python[2]["last_name"])

# Change "John" to "Johnathan".
monty_python[1]["first_name"] = "Johnathan"
pprint(monty_python)

instrument_brands = {
    "electric_guitars": ["Les Paul", "Fender", "PRS"],
    "banjos": ["Deering", "Gold Tone"],
    "ukuleles": ["Kamaka", "Koaloha", "Kanilea"],
}

# Add another key to the dictionary - "acoustic_guitars".
# Make its value an empty list.

print("before:", instrument_brands)
instrument_brands["acoustic_guitars"] = []
print("after:", instrument_brands)

# Add "Martin" and "Taylor" to the acoustic_guitars list.
instrument_brands["acoustic_guitars"].append("Martin")
instrument_brands["acoustic_guitars"].append("Taylor")
print(instrument_brands)

# Getting and Setting Values in Nested Lists
# Print "Deering".
print(instrument_brands["banjos"][0])
# Change "PRS" to "Paul Reed Smith".
instrument_brands["electric_guitars"][2] = "Paul Reed Smith"
print(instrument_brands)


"""
=== === LET'S LOOP! === ===
"""

# Loop through the Monty Python list, printing each key of
# each nested dictionary
for each_dictionary in monty_python:
    for each_key in each_dictionary:
        print(each_key)

# Loop through the Monty Python list, printing each value of
# each nested dictionary
for each_dictionary in monty_python:
    for each_key in each_dictionary:
        print(each_dictionary[each_key])

# Loop through the Monty Python list, printing each key and
# value of each nested dictionary
for each_dictionary in monty_python:
    for each_key in each_dictionary:
        print(f"{each_key}: {each_dictionary[each_key]}")

# Loop through the instrument_brands dictionary, printing
# the length of each nested list
for each_key in instrument_brands:
    print(len(instrument_brands[each_key]))

# Loop through the instrument_brands dictionary, printing
# each value of each nested list
for each_key in instrument_brands:
    for brand in instrument_brands[each_key]:
        print(brand)

# Loop through the instrument_brands dictionary, printing
# the length of each nested list, each key, and each value
for each_key in instrument_brands:
    print(len(instrument_brands[each_key]), each_key)
    for brand in instrument_brands[each_key]:
        print(brand)

# Expected output:
"""
3 electric_guitars
Les Paul
Fender
Paul Reed Smith

2 banjos
Deering
Gold Tone

3 ukuleles
Kamaka
Koaloha
Kanilea

2 acoustic_guitars
Martin
Taylor
"""
