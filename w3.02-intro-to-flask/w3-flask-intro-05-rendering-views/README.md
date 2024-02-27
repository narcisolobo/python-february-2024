- [Rendering Templates](#rendering-templates)
  - [Create a New Project](#create-a-new-project)
  - [Create a View](#create-a-view)
  - [The `templates` Directory](#the-templates-directory)
  - [The `render_template` Function](#the-render_template-function)
  - [Give it a Whirl!](#give-it-a-whirl)
  - [Add More Routes and Templates](#add-more-routes-and-templates)
  - [Summary](#summary)


# Rendering Templates
Up to now, we've been returning strings from our view functions. Of course, this is not ideal. Let's learn how to use the templating system built into Flask.

## Create a New Project

Create a new project. In the project root, install Flask in the project's virtual environment and activate it.

```shell
mkdir my_cool_site
cd my_cool_site
pipenv install Flask
pipenv shell
```

Inside the project root, create a `server.py` file and write a simple Flask app.

```py
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
```

## Create a View

Create a view that maps a function to the root route: `"/"`. In the example below, we're naming this function `index()`, but you can name it whatever you like.

For now, let's leave this function as a placeholder stub using the `pass` keyword.

```py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
  """This is the root route view."""
  pass


if __name__ == "__main__":
    app.run(debug=True)
```

## The `templates` Directory
In order to return HTML from a view function, we must first create a `templates` folder in the root of our project (at the same level as `server.py`).

***Important:** The directory must be named `templates`, plural and lower case. Flask will not find it if this is not the case.*

The `templates` directory is where we will place all of our Jinja templates. These templates have `.html` file extensions, just like we're used to.

Go ahead and create a file, `index.html`. In this file, create an `<h1>` element with some content.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Cool Site - Home</title>
  </head>
  <body>
    <h1>Hello world!</h1>
  </body>
</html>
```

## The `render_template` Function

The process of responding with HTML instead of merely a string is quite straightforward. Flask makes it pretty easy for us, if we follow the steps.

Back in `server.py`, we'll first need to import a function from Flask called `render_template`.

```py
from flask import Flask, render_template
# rest of code removed for brevity
```

This function allows our Flask server to return HTML as a response to the client.

Let's now revisit our `index()` view function. Replace the `pass` keyword with a `return` statement. We will return a function call to `render_template`. In the function arguments, we'll pass the path to the appropriate template, relative to the `templates` directory, as a string.

```py
# code removed for brevity

@app.route("/")
def index():
  return render_template("index.html")

# code removed for brevity
```

## Give it a Whirl!

That's it! Let's spin up our server. In the terminal, `cd` into the project root (if you're not already there) and execute `python server.py` to spin up our dev server.

In your browser, navigate to `http://localhost:5000`. You should see the HTML we created.

If you do not see what you expect - *play the "matchy-matchy" game*.

- Is your `templates` folder named "templates"? It must be plural and lower case.
- Is the path to the template correct? Check the template's filename and compare it to the path you passed to `render_template`.

## Add More Routes and Templates

Let's add another view! Create a view function that handles a request to the `/about` route and responds with a new `about.html` template.

Do the same for `/services` and `/contact`.

## Summary

In this lesson, we explored how to render templates in Flask, moving beyond returning simple strings from our view functions and taking another step towards generating dynamic HTML content. Here's a quick recap of what we covered:

- We started by creating a new Flask project and setting up a basic Flask app structure.
- Next, we created a view function for the root route (`"/"`) and learned about the importance of the `templates` directory in our project structure.
- We created our first HTML template (index.html) and stored it in the `templates` directory.
- Using Flask's `render_template` function, we connected our view function to the HTML template, allowing us to return HTML responses.
- Finally, we tested our setup by spinning up the Flask development server and accessing our routes in the browser.

Remember, as you continue to build your Flask applications, understanding how to effectively render templates will be essential for creating dynamic web pages. Don't hesitate to experiment further with Flask's templating capabilities and explore more advanced features to take your projects to the next level. I recommend [Jinja's template inheritance features](https://flask.palletsprojects.com/en/2.3.x/patterns/templateinheritance/).
