"""
=== === LOOPS AND DICTIONARIES === ===

Dictionaries are also iterable. When we iterate through a
dictionary, the iterator is each key of the dictionary.
"""

strat = {
    "brand": "Fender",
    "model": "Stratocaster",
    "year": 1977,
    "color": "blue",
    "is_new": False,
}

for each_key in strat:
    print(each_key)

for each_key in strat:
    print(strat[each_key])

"""
=== === DICTIONARY METHODS === ===
There are many useful methods we can use with lists.

keys(), values(), items()

.keys() - returns a list of the dictionary's keys.
.values() - returns a list of the dictionary's values.
.items() - returns a list of tuples of the dictionary's key-value pairs.
"""
