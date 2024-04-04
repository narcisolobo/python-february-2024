# Python Decorators

- [Python Decorators](#python-decorators)
  - [First-Class Objects](#first-class-objects)
    - [Inner Functions](#inner-functions)
    - [Functions As Return Values](#functions-as-return-values)
  - [Simple Decorators in Python](#simple-decorators-in-python)
    - [Adding Syntactic Sugar](#adding-syntactic-sugar)


In this lesson on Python decorators, we'll learn what decorators are and how to create and use them. Decorators provide a simple syntax for calling higher-order functions.

By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it. This sounds confusing, but it'll make more sense after we've seen a few examples of how decorators work.

In this lesson, we'll learn:

- What it means for functions to be first-class objects
- How to define functions so they can be used as decorators
- Which practical use cases can be tackled with decorators
- How to create decorators so that they follow best practices

## First-Class Objects

In Python, functions are treated as first-class objects.

This means that functions can be passed around and used as arguments, just like any other object like str, int, float, list, and so on.

Consider the following three functions:

```py
def friend(name):
    print(f"What's happening, {name}?")


def stranger(name):
    print(f"Hello, {name}.")


def greet(greet_func, name):
    greet_func(name)
```

Here, `friend()` and `stranger()`  are regular functions that expect a name given as a string.

The greet() function, however, expects a function and a name as its arguments.

We can, for example, pass it the `friend()` or the `stranger()`
function.

```py
greet(stranger, "Shirley")
greet(friend, "Bob")
```

Note that `greet()` refers to two functions, but in different ways: `greet()` and `friend`. The `friend` function is named *without* parentheses.

This means that only a reference to the function is passed. The function isn't executed.

The `greet()` function, on the other hand, is written *with* parentheses, so it will be called as usual.


### Inner Functions

It's possible to define functions inside other functions.

Such functions are called *inner functions*. Here's an example of a function with two inner functions:

```py
def parent():
    print("Printing from parent()")

    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")

    second_child()
    first_child()
```

What happens when we call the `parent()` function? Think about this for a minute.

### Functions As Return Values

Python also allows we to *return functions from functions*. In the following example, we rewrite `parent()` to return one of the inner functions:

```py
def parent(num):
    def first_child():
        print("Hi, I'm Venus.")

    def second_child():
        print("Call me Serena.")

    if num == 1:
        return first_child
    else:
        return second_child
```

Note that we're returning `first_child` *without* the parentheses. Recall that this means that we're returning a *reference* to the function `first_child`.

In contrast, `first_child()` *with* parentheses refers to the result of evaluating the function.

We can see this in the following example:

```py
first = parent(1)
second = parent(2)

print(first)
# <function parent.<locals>.first_child at 0x1024e71a0>
print(second)
# <function parent.<locals>.second_child at 0x1024e7380>
```

The somewhat cryptic output means that the first variable refers to the local `first_child()` function inside of `parent()`, while second points to `second_child()`.

We can now use first and second as if they're regular functions, even though we can't directly access the functions they point to:

```py
first()
second()
```

Note that in the earlier example, we executed the inner functions within the parent function—for example, `first_child()`.

However, in this last example, we didn't add parentheses to the inner functions, such as `first_child`, upon returning. 

That way, we got a reference to each function that we could call in the future.

## Simple Decorators in Python
Now that we've seen that functions are just like any other object in Python, we're ready to move on and see the magical beast that is the Python decorator. We'll start with an example:

```py
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def homer():
    print("Woo hoo!")**


homer = decorator(homer)
```
Here, we've defined two regular functions, `decorator()` and `homer()`, and one inner `wrapper()` function. Then we redefined `homer()` to apply `decorator()` to the original `homer()`.

Can we guess what happens when we call `homer()`?

```py
homer()
# Something is happening before the function is called.
# Woo hoo!
# Something is happening after the function is called.
```

To understand what's going on here, look back at the earlier examples. We're applying everything that we've learned so far.

The so-called decoration happens at the following line:

```py
homer = decorator(homer)
```

In effect, the name `homer` now points to the `wrapper()` inner function. Remember that you return `wrapper` as a function when you call `decorator(homer)`.

However, `wrapper()` has a reference to the original `homer()` as `func`, and it calls that function between the two calls to `print()`.

Put simply, *a decorator wraps a function, modifying its behavior.*

### Adding Syntactic Sugar
The way we decorated `homer()` is a little clunky. First of all, we end up typing the name `homer` three times. Additionally, the decoration gets hidden away below the definition of the function.

Instead, Python allows us to use decorators in a simpler way with the `@` symbol, sometimes called the pie syntax. The following example does the exact same thing as the decorator example:

```py
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def homer():
    print("Woo hoo!")
```

So, `@decorator` is just a shorter way of saying `homer = decorator(homer)`. It's how we apply a decorator to a function.