# Flask Routing and View Functions

Flask is a web application framework for Python that follows the concept of routing and view functions. These two components play a crucial role in defining the behavior and structure of your web application.

## Routing:
Routing refers to the process of mapping URL requests to specific functions in your Flask application. It determines how different URL requests will be handled and which code will execute when a particular URL is requested.

### Decorators `@app.route()`
In Flask, routing is achieved through the use of decorators, specifically the `@app.route()` decorator.

#### Static routing
```py
@app.route("/home")
def home():
  return "This is the home view."
```
#### Dynamic routing with route parameters
```py
@app.route("/projects/<int:project_id>")
def project_details(project_id):
  return f"Viewing project {project_id}."
```

### View Functions:
View functions are Python functions that are associated with specific routes. When a user requests a particular URL, Flask calls the corresponding view function to handle the request and generate the response. View functions define what content is displayed or what actions are performed when a specific URL is accessed.
