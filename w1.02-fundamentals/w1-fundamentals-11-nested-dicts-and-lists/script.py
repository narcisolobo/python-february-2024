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

# Add Michael Palin to the list.

# Getting and Setting Values in Nested Dictionaries
# Print "Gilliam".
# Change "John" to "Johnathan".

instrument_brands = {
    "electric_guitars": ["Les Paul", "Fender", "PRS"],
    "banjos": ["Deering", "Gold Tone"],
    "ukuleles": ["Kamaka", "Koaloha", "Kanilea"],
}

# Add another key to the dictionary - "acoustic_guitars".
# Make its value an empty list.

# Add "Martin" and "Taylor" to the acoustic_guitars list.

# Getting and Setting Values in Nested Lists
# Print "Deering".
# Change "PRS" to "Paul Reed Smith".

"""
=== === LET'S LOOP! === ===
"""

# Loop through the Monty Python list, printing each key of
# each nested dictionary

# Loop through the Monty Python list, printing each value of
# each nested dictionary

# Loop through the Monty Python list, printing each key and
# value of each nested dictionary

# Loop through the instrument_brands dictionary, printing
# the length of each nested list

# Loop through the instrument_brands dictionary, printing
# each value of each nested list

# Loop through the instrument_brands dictionary, printing
# the length of each nested list, each key, and each value

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
