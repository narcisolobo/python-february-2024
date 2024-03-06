INSERT INTO users (first_name, last_name, email, password)
VALUES
("Etta", "James", "etta@atlast.com", "atlast"),
("Bill", "Withers", "bill@stillbill.com", "aintnosunshine"),
("Gladys", "Knight", "gladys@thepips.com", "midnighttrain");

SELECT * FROM users;

SELECT * FROM users WHERE id=3;

UPDATE users
SET email = "gladys@gladysknight.com"
WHERE id = 4;

UPDATE users
SET first_name = "Robert", last_name = "Marley Edited", email = "robert@marley.com", password = "onelove"
WHERE id = 1;

DELETE FROM users
WHERE id = 4;

INSERT INTO users (first_name, last_name, email, password)
VALUES
("Gladys", "Knight", "gladys@thepips.com", "midnighttrain");