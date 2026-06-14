DROP TABLE IF EXISTS dinoscores;

CREATE TABLE IF NOT EXISTS dinoscores(
    sn INTEGER,
    name TEXT,
    score INTEGER
);


-- insert data
INSERT INTO dinoscores(sn,name,score) VALUES(1, 'Jhud', 20);
INSERT INTO dinoscores(sn,name,score) VALUES(2, 'Akash', 19);
INSERT INTO dinoscores(sn,name,score) VALUES(3, 'Bob', 30);

-- insert multiple lines at once
INSERT INTO dinoscores(sn,name,score) VALUES(4, 'John', 50), (5, 'Billy', 30);

-- display data
SELECT * FROM dinoscores;


-- display names only
SELECT name FROM dinoscores;
-- display names and scores only
SELECT name,score FROM dinoscores;
-- display names and scores only above 30
-- where clause
SELECT name,score FROM dinoscores WHERE score > 30;
-- naming columns
SELECT name AS 'Playername', score FROM dinoscores;
-- AGGREGATE functions: MAX, MIN, COUNT, AVG and ADD
-- Most = MAX()
-- Least = MIN()
-- Average = AVG()
-- Add things together = ADD()




-- Updating 
UPDATE dinoscores set score = 100 WHERE name = 'Jhud'

-- delete part of TABLE
DELETE FROM dinoscores WHERE name = 'Akash'

-- delete whole table 
/* DROP TABLE dinoscores; */

-- select users starting or ending or containing with a certain letter
-- % means everyything else, so %a% will display everythnig with an a in it

SELECT * FROM dinoscores WHERE name LIKE '%a%'

-- order by shows a column in ascending value 
-- DESC means descending and goes before semi colon

SELECT * FROM dinoscores ORDER BY score desc;

-- group by creates a table of what you want to group
-- writing as ... changes the name of tyhe column

SELECT score, count(*) as 'number of people' FROM dinoscores GROUP BY score;

-- top 2 scores
-- LIMIT x will display the top x players

SELECT * FROM dinoscores ORDER BY score DESC LIMIT 2;

-- cross join is when you take info from multiple tables
-- we don't have multiple tables so I will use the same names as on the online SQL compiler
-- if crossjoin is applied to rows a, b and c,  we get ab, ac and bc
-- something like this might happen:

/*select * from customers JOIN orders on Customers.customer_id = Orders.order_id;*/

--more than two tables:

/* select * from customers JOIN shippings on Customers.customer_id = Shippings.shipping_id JOIN Orders 
on Customers.customer_id = Orders.order_id; */