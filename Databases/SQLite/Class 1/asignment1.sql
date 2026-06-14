CREATE TABLE STUDENT (
    roll_no TEXT,
    name TEXT,
    address TEXT,
    phone TEXT,
    age INTEGER
);

INSERT INTO STUDENT (roll_no, name, address, phone, age) VALUES
('1', 'Oliver Smith', 'London', '+44 7700 900001', 14),
('2', 'Emily Johnson', 'Manchester', '+44 7700 900002', 15),
('3', 'Harry Brown', 'Birmingham', '+44 7700 900003', 16),
('4', 'Amelia Wilson', 'Leeds', '+44 7700 900004', 14),
('5', 'Noah Taylor', 'Bristol', '+44 7700 900005', 17),
('6', 'Sophia Davies', 'Nottingham', '+44 7700 900006', 15),
('7',  'Emily Johnson',   'London',      '07XXXXXXX1', 15),
('8',  'Oliver Smith',    'Manchester',  '07XXXXXXX2', 14),
('9',  'Sophia Davies',   'London',      '07XXXXXXX3', 16),
('10', 'Harry Brown',     'Birmingham',  '07XXXXXXX4', 17),
('11', 'Amelia Wilson',   'Leeds',       '07XXXXXXX5', 14),
('12', 'Jack Taylor',     'London',      '07XXXXXXX6', 18),
('13', 'Isla Thompson',   'Manchester',  '07XXXXXXX7', 15),
('14', 'Noah Anderson',   'Bristol',     '07XXXXXXX8', 16),
('15', 'Mia Thomas',      'London',      '07XXXXXXX9', 13),
('16', 'Leo Martin',      'Leeds',       '07XXXXXX10', 17),
('17', 'Ella White',      'Birmingham',  '07XXXXXX11', 15),
('18', 'James Harris',    'London',      '07XXXXXX12', 16),
('19', 'Lily Clark',      'Manchester',  '07XXXXXX13', 14),
('20', 'Ben Lewis',       'Bristol',     '07XXXXXX14', 18),
('21', 'Chloe Walker',    'London',      '07XXXXXX15', 15);

SELECT * FROM STUDENT
WHERE age = 15 AND address = 'London';

SELECT * FROM STUDENT
WHERE name = 'Emily Johnson' AND age = 15;

SELECT * FROM STUDENT
WHERE name = 'Oliver Smith' OR name = 'Sophia Davies';

SELECT * FROM STUDENT
WHERE name = 'Harry Brown' OR age = 17;

SELECT * FROM STUDENT
WHERE age = 14 AND (name = 'Oliver Smith' OR name = 'Amelia Wilson');
