# POST Form Submission

Up to now, we've been handling requests and writing view functions for a specific type of request, a `GET` request. When the user clicks a hyperlink or types a URL in the address bar, the browser sends one of these `GET` requests to our Flask server.

Today, we'll be handling a different type of request made by the browser, a `POST` request.

## `GET` vs. `POST`

To illustrate the difference, imagine you're ordering food online. When you click on a menu item to see its details (like ingredients or price), you're making a `GET` request. You're asking the server to give you information about that specific menu item.

Now, when you're ready to place your order, you fill out a form with your name, address, and the items you want to order. When you click the "Submit" button, you're making a `POST` request. You're sending all that information to the server so it can process your order.

So, in simple terms:

- a `GET` request is like asking for information.
- a `POST` request is like sending information to be processed.

## Handling `POST` Requests
There will be three routes involved in handling `POST` requests.
- A route to display the form.
  ```py
  @app.route("/survey/show")
  def survey():
      return render_template("form.html")
  ```
- A route to process the form.
  ```py
  @app.route("/survey/process", methods=["POST"])
  def process():
      return redirect("/survey/results")
  ```
- A route to display the results.
  ```py
  @app.route("/survey/results")
  def results():
      return render_template("results.html")
  ```

### A Closer Look
Let's take a closer look at the `POST` handler view function.
```py
@app.route("/survey/process", methods=["POST"])
def process():
    return redirect("/survey/results")
```
**The methods argument:** The first difference we notice here is the addition of another argument passed to the `@app.route` decorator, a named argument called `methods`.

The `@app.route` decorator handles `GET` requests by default. In order to handle `POST` requests, we must explicitly say so. Notice `methods` is plural, and its value is a list.
```py
@app.route("/survey/process", methods=["POST"])
```

There is an alternative shorthand to this syntax that I personally prefer:
```py
@app.post("/survey/process")
```
I'll be using the alternative syntax often going forward.

**The redirect method:** The other difference we see here is the invocation of a different function in our `return` statement.
```py
    return redirect("/survey/results")
```
This method sends a `GET` request on behalf of the user to the route we pass in as an argument. **Note that we pass in a route, not a template.** The user will be redirected to the route we specify.

In order to use this method, remember to import it from the flask package at the top of your file.
```py
from flask import Flask, redirect, render_template
```

### Do Not Render on a `POST` Request
Can you think of why it might be a bad idea to render a template in this `POST` handler? What if the user filled out a form to purchase a product? What if this view function is handling a registration form? What if the user is adding a pet to our "Boops" app?

## The `request.form` Dictionary
When a user clicks submit on a form, Flask packages the form data into a dictionary for us. This dictionary can be found in the `form` attribute of the `request` object.

In order to pull the form data out of the `request` object, we must import it at the top of our file.

```py
from flask import Flask, redirect, render_template, request
```

Once imported, we can use it in any `POST` handling view function.

```py
@app.route("/survey/process", methods=["POST"])
def process():
    print(request.form)
    return redirect("/survey/results")
```

In the above snippet, we're just printing the form data dictionary. Let's see what that print out would look like.

If our form looked like this:
```html
<!-- survey.html -->
<form action="/survey/process" method="POST">
  <label>First name:</label>
  <input type="text" name="first_name" />
  <label>Last name:</label>
  <input type="text" name="last_name" />
  <label>Age:</label>
  <input type="number" name="age" />
</form>
```

And the user had entered "Rick", "Sanchez", and "70" into the form inputs, the `request.form` dictionary would look like this:

```py
{
  "first_name": "Rick",
  "last_name": "Sanchez",
  "age": "70"
}
```

As we can see, Flask creates this dictionary with key names that match the `name` attributes of our inputs. The values are the user's entries.

Knowing this, we can now print each value if we like.

```py
@app.route("/survey/process", methods=["POST"])
def process():
    print(request.form["first_name"]) # "Rick"
    print(request.form["last_name"]) # "Sanchez"
    print(request.form["age"]) # "70"
    return redirect("/survey/results")
```

Note that even though the age input type was `number`, the value in the `request.form` dictionary is a string. If we need it to be an integer or float, we must cast it as so.

```py
print(int(request.form["age"])) # 70
```
