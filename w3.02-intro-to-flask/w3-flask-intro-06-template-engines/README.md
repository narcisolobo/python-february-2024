# Template Engines

Template engines are tools used in web development to generate *dynamic* HTML content by combining data with predefined HTML templates. They simplify the process of building web pages by allowing developers to separate the structure of the webpage from its content.

## Key Features of Template Engines

1. **Template Syntax:** Template engines typically provide their own syntax for embedding dynamic content within HTML templates. This syntax allows developers to insert variables, conditionals, loops, and other logic into the template.

2. **Data Binding:** Template engines facilitate the binding of data to the HTML template. Data can be sourced from various places such as databases, APIs, or user inputs, and then injected into the template to produce the final output.

3. **Reusability:** Templates promote code reusability by allowing developers to define reusable components or layouts. This modular approach simplifies maintenance and encourages a more structured development process.

## Flask Templating and Jinja2
Flask uses a templating engine named Jinja2. Jinja2 is a powerful template engine for Python. It offers a flexible syntax and advanced features such as template inheritance and macros.

### Jinja2 Syntax:
Templates in Flask are Jinja-HTML files with *placeholders* that can be dynamically filled with data.

Jinja2 employs a special syntax for variable interpolation and control flow statements like `for` loops and `if` statements.

- Use double curly braces `{{ variable }}` to display the value of variables.

- Use single curly braces and percent signs `{% for item in items %}...{% endfor %}` for loops and conditionals.
### Variable Interpolation
```html
<h1>Welcome, {{ user.first_name }}!</h1>
```

```html
<h1>Your Dog Details:</h1>
<p>Name: {{ dog.name }}</p>
<p>Breed: {{ dog.breed }}</p>
<p>Age: {{ dog.age }}</p>
```

### Logic and Control Structures
#### For loops
```html
{% for product in products %}
    <p>{{ product.name }}</p>
    <p>{{ product.price }}</p>
{% endfor %}
```

#### Conditionals
```html
{% if product.quantity > 0 %}
    <p>{{ product.quantity }}</p>
{% else %}
    <p>Out of stock</p>
{% endif %}
```

### Filling In Placeholders with Values

We fill in placeholders with values by passing variables in the `render_template` function.

**Syntax:**
```py
render_template("template_name.html", variable=value)
```

**Example:**
```py
# dashboard view function
@app.route("/dashboard")
def dashboard():
   return render_template("dashboard.html", message="Welcome!") 
```

```html
<!-- dashboard.html -->
<h1>{{ message }}</h1>
```

### Using Values From the Route

**Example:**
```py
# product_details view function
@app.route("/products/<int:product_id>")
def product_details(product_id):
   return render_template("product_details.html", product_id=product_id) 
```

```html
<!-- product_details.html -->
<h1>You are viewing product no. {{ product_id }}</h1>
```