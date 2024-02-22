"""
=== === LISTS === ===
In Python, arrays are called lists. 

Lists are ordered and changeable.

Lists allow duplicate values.
"""

# List creation
colors = ["red", "green", "rebeccapurple"]

# List indices
"""
Lists have indices just like arrays have indices in
JavaScript. They are also zero-indexed as well.
"""
print(colors[1])

# List negative indices
"""
Python supports negative indices. A -1 index will refer
to the last element in a list.
"""
print(colors[-1])
# print(colors[-4])  # error index out of range

print("are these the same?")
print(colors[1])
print(colors[-2])


# Common list methods
"""
There are many useful methods we can use with lists.
"""

# length
"""
Pass a list to the len() method to return the number of
elements in the list.
"""

print(len(colors))

# append, remove, pop
"""
append() - adds an element to the end of a list.
remove() - removes the specified element from a list.
pop() - removes the element at the specified position
"""
colors.append("coral")
print(colors)
colors.insert(1, "gold")
print(colors)

colors.remove("green")
print(colors)

# colors.remove("blue")
print(colors)

print("before:", colors)
last_item = colors.pop()
print("after:", colors)
print(last_item)

print("before:", colors)
colors.pop(0)
print("after:", colors)

# sort, reverse
"""
The sort() method sorts a list in ascending order in-place.
The reverse() method reverses a list.
"""

fibonacci = [1, 1, 2, 0, 5, 8, 13, 3]
result = fibonacci.sort()
print(result)
print(fibonacci)

fibonacci.reverse()
print(fibonacci)

new_list = [5, 2, 8]
new_list.reverse()
print(new_list)


# Explore more list methods!
# https://www.w3schools.com/python/python_ref_list.asp
