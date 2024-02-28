# Static Files in Flask

Some components of our Flask applications are static. Files like CSS style sheets, JavaScript files, and images are some examples of static components. Their content does not change.

For these files, we will use a special built-in Flask function called `url_for`.

## The Static Directory

At the project root (the same level as `server.py` and the `templates` folder) we will create a new directory named `static`.

Following best practices, let's also create a `css` folder, a `js` folder, and an `images` folder inside the `static` folder.

Place the appropriate files in their respective directories.

```
project/
├── server.py
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── script.js
│   ├── images/
│   │   ├── f-string.jpg
│   │   └── logo.png
└── templates/
    ├── index.html
    └── about.html
```

## Using Static Assets in Flask Templates

Whenever we need to display or link to a static asset, we will use the `url_for` function built into Flask. We will call this function in our Jinja templates.

### Syntax
```py
url_for('static', filename='/path/to/file')
```

### Examples
**CSS:**
```html
<link rel="stylesheet" href="url_for('static', filename='/css/style.css')" />
```

**JavaScript:**
```html
<script src="url_for('static', filename='/js/script.js')"></script>
```

**Images:**
```html
<img src="url_for('static', filename='/images/logo.png')" />
```

[Click here for the exercise.](./exercise.md)