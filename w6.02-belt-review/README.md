# Python Belt Exam Guidelines
I highly recommend that you prepare your exam project in advance. You should at least have a working login and registration component already tested and working. Have at least one user registered in your database.

An orange or red belt will require implementation of a one-to-many relationship between users and some other table. This other table cannot be pre-coded, but it can be generated from boilerplate templates that you prep beforehand. Use the replace all feature in VS Code and remember to preserve case.

Once you create the second table, seed it with at least one or two rows.

A black belt will require implementation of a many-to-many relationship. For practice, you can add a "likes" or "favorites" feature to the [Coding Dojo Wall assignment](https://login.codingdojo.com/m/506/12465/87451) and/or the [Recipes assignment](https://login.codingdojo.com/m/506/12466/87454). The [Ohana Rideshares assignment](https://login.codingdojo.com/m/506/12466/96503) already includes a many-to-many relationship.

## Project Directory Structure
Screen shot of typical directory structure:

![flask app structure](./assets/flask-app-structure.png)

## Preparation Checklist
- [ ] Working Login/Registration
- [ ] Boilerplate model class for the child table (gizmo.py)
- [ ] Boilerplate controller for the child table (gizmos.py)
- [ ] Boilerplate HTML templates

### Create Code Flow
**Prep:**
1. GET route that displays form
2. HTML template with form:
   1. Form element must have an action and a method
   2. Action defines the form processing route
   3. Method must be "POST"
   4. Every placeholder in your SQL query must have corresponding `name` attributes in your form
   5. This includes a hidden input for the logged-in user's id (`user_id`).
   6. A submit button INSIDE the form

**Submit Flow:**
1. User submits form as POST request to the processing route
2. Processing POST handler in controller receives request
3. Validator static method is called
4. Validator checks each input for validity in series of `if elif` blocks and returns a boolean value of `True` or `False`
5. Back in controller, if validator function returns `False`, redirect the user back to form and display error messages
6. Repeat steps 1-5 until validator returns `True`
7. If validator returns `True`, create new row in database by calling the `create` class method (the platform calls it `save`).
8. The `create` class method must have a SQL `INSERT` query with placeholders that match the `name` attributes for the inputs in your form
9. `connectToMySql` function is called
10. `query_db` is chained and called, and we pass the query and `form_data` to it
11. `query_db` returns the id of the row it created for `INSERT` queries (or `False` if your query fails)
12. Back in controller, we can use the id that was returned from `query_db` to redirect the user to the details route
13. Or we can just redirect the user to the route that displays all (this is what will usually be the case)

### Update Code Flow
**Prep:**
1. GET route that displays form
2. HTML template with form:
   1. Form element must have an action and a method
   2. Action defines the form processing route
   3. Method must be "POST"
   4. Every placeholder in your SQL query must have corresponding `name` attributes in your form
   5. This may include a hidden input for the id of the row you're updating (`gizmo_id`).
   6. A submit button INSIDE the form

**Submit Flow:**
1. User submits form as POST request to the processing route
2. Processing POST handler in controller receives request
3. Validator static method is called
4. Validator checks each input for validity in series of `if elif` blocks and returns a boolean value of `True` or `False`
5. Back in controller, if validator function returns `False`, redirect the user back to form and display error messages
6. Repeat steps 1-5 until validator returns `True`
7. If validator returns `True`, update the existing row in database by calling the `update` class method.
8. The `update` class method must have a SQL `UPDATE` query with placeholders that match the `name` attributes for the inputs in your form
9. `connectToMySql` function is called
10. `query_db` is chained and called, and we pass the query and `form_data` to it
11. `query_db` returns `None` for `UPDATE` queries (or `False` if your query fails)
12. Back in controller, we use the `gizmo_id` from the form to redirect the user to the details route
