## Accessing values with bracket notation

We can access values in a dictionary by their
key names. Use bracket notation with quotes.

```py
print(strat["year"])  # 1977
```

## Accessing values with the get() method

We can access values in a dictionary with the get()
method. Pass the key name in the method call in quotes.

```py
print(strat.get("is_new"))  # False
```

> What's the difference between bracket notation and .get()?  
> With .get(), our application doesn't break if we specify a key name that doesn't exist.

```py
# print(strat["non_existent_key"])  # KeyError: 'non_existent_key'
print(strat.get("non_existent_key"))  # None
```

## Dictionary methods
There are many useful methods we can use with lists.

### keys, values, items

- `.keys()` - returns an array of the dictionary's keys.
- `.values()` - returns an array of the dictionary's values.
- `.items()` - returns an array of tuples of the dictionary's key-value pairs.

```py
print(strat.keys())  # dict_keys(['brand', 'model', 'year', 'color', 'is_new'])
print(strat.values())  # dict_values(['Fender', 'Stratocaster', 1977, 'blue', False])
print(strat.items())
# dict_items([('brand', 'Fender'), ('model', 'Stratocaster'), ('year', 1977), ('color', 'blue'), ('is_new', False)])
```

### in, not in

We can use the 'in' and 'not in' keywords to check if a key
name exists in a dictionary.

```py
if "color" in strat:
    print("color exists in strat")

if "banana" not in strat:
    print("banana not in strat")
```

[Explore more dictionary methods!](https://www.w3schools.com/python/python_ref_dictionary.asp)