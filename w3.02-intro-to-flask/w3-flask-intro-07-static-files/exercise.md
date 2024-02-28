# Dynamic Templates Exercise

**Set up:**
1. Review the concept of variable rules in Flask routes.
2. Set up a new Flask project named "f-string".
3. Create a template named `index.html`.
4. Create an `<h1>` element on the page with the content, "F String Baybeeehh!".
5. Create an `<img>` element on the page to display the "F String Baybeeehh" gif. The image should live in `static/images/`.
6. Custom CSS should be in a `static/css/` folder. Use the `url_for` function to `<link>` the file in the `<head>` of your HTML.
7. Create a `<style>` tag in the `<head>` of your HTML. In the tag, change the body's background color to `blanchedalmond`.

**Goals:**
1. Create the following Flask routes in your server.py file:
   1. Route `/`: Render the `index.html` template as is.
   2. Route `/<new_heading>`: Render the `index.html` template with a custom heading specified by the URL parameter `new_heading`. Use this parameter to dynamically change the `<h1>` heading of the template.
   3. Route `/<new_heading>/<body_color>`: Render the `index.html` template with a custom heading *and* a custom background color specified by the URL parameter `body_color`. Use this parameter to dynamically change the background color of the `<body>` element.
   4. Route `/<new_heading>/<body_color>/<int:num>`: Render the `index.html` template with a custom heading, a custom background color *and* a custom number of images specified by the URL parameter `num`. Use this parameter to dynamically configure the number of `<img>` elements in the rendered HTML.
2. Test your application by visiting each of the created routes(`/`, `/<new_heading>`, `/<new_heading>/<body_color>`, `/<new_heading>/<body_color>/<int:num>`) in a web browser. onbserve how the template dynamically changes based on the URL parameters.
3. Experiment with different values for the URL parameters to see how they affect the rendered HTML.

**Bonus:** Use a [classless CSS framework](https://blog.logrocket.com/comparing-classless-css-frameworks/) to enhance the look of the page.