DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER,
    name TEXT,
    age INTEGER,
    address TEXT
);

INSERT INTO students VALUES (1, 'Alif Azhar', 14, 'London');
INSERT INTO students VALUES (2, 'Emily Johnson', 15, 'London');
INSERT INTO students VALUES (3, 'Noah Smith', 16, 'Manchester');
INSERT INTO students VALUES (4, 'Oliver Brown', 15, 'Leeds');
INSERT INTO students VALUES (5, 'Sophia Wilson', 14, 'Manchester');
INSERT INTO students VALUES (6, 'Liam Davis', 15, 'London');
INSERT INTO students VALUES (7, 'Amelia Taylor', 16, 'Leeds');
INSERT INTO students VALUES (8, 'James Anderson', 15, 'Manchester');

SELECT age, name FROM students;

SELECT * FROM students WHERE address = 'London';

SELECT * FROM students WHERE age = 15 AND address = 'London';

SELECT * FROM students WHERE address = 'London' OR address = 'Manchester';

UPDATE students SET address = 'London' WHERE roll_no = 3;

DELETE FROM students WHERE roll_no = 8;

SELECT name, age FROM students ORDER BY age ASC;

SELECT COUNT(*) as number FROM students WHERE address = 'Manchester';

SELECT AVG(age) FROM students WHERE address = 'London';

SELECT COUNT(*) as 'number' FROM students WHERE name LIKE '%n%' OR name LIKE '%N%';

SELECT address, COUNT(*) as 'number' FROM students GROUP BY address;

SELECT age, COUNT(*) as 'number' FROM students GROUP BY age;

SELECT address, age, COUNT(*) as 'number' FROM students GROUP BY address, age;
