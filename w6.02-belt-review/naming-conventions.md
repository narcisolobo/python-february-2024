# Naming Conventions

## MySQL
| Type        | Convention                             | Examples                   |
| ----------- | -------------------------------------- | -------------------------- |
| Schema Name | snake case, ending in `db` or `schema` | `myths_db`, `pets_schema`  |
| Table Name  | snake case, plural                     | `album_tracks`, `users`    |
| Primary Key | lowercase                              | `id`                       |
| Foreign Key | snake case, singular, ending in `id`   | `user_id`                  |
| Column Name | snake case                             | `first_name`, `created_at` |

## Flask App
| Type                | Convention            | Examples                 |
| ------------------- | --------------------- | ------------------------ |
| Model Filename      | lowercase, singular   | `user.py`, `recipe.py`   |
| Class Name          | pascal case, singular | `User`, `Recipe`         |
| Controller Filename | snake case, plural    | `users.py`, `recipes.py` |

### Controller View Functions
| Description         | Route                             | HTTP Method | Function Name   |
| ------------------- | --------------------------------- | ----------- | --------------- |
| Display Create Form | `/recipes/new`                    | get         | `new_recipe`    |
| Process Create Form | `/recipes/create`                 | post        | `create_recipe` |
| Find All            | `/recipes` or `/recipes/all`      | get         | `all_recipes`   |
| Find One            | `/recipes/<int:recipe_id>`        | get         | `show_recipe`   |
| Display Update Form | `/recipes/<int:recipe_id>/edit`   | get         | `edit_recipe`   |
| Process Update Form | `/recipes/<int:recipe_id>/update` | post        | `update_recipe` |
| Delete              | `/recipes/<int:recipe_id>/delete` | post or get | `delete_recipe` |