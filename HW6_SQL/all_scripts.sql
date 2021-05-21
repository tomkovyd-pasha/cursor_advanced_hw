USE my_items;

-- create TABLE phone_companies
/*
CREATE TABLE phone_companies (
	id INT NOT NULL AUTO_INCREMENT
	,name VARCHAR(255)
	,PRIMARY KEY (id)
);
*/

-- create TABLE phones
/*
CREATE TABLE phones (
	id INT NOT NULL AUTO_INCREMENT
	,phone_name VARCHAR(255)
	,company_id INT NOT NULL
	,user_id INT NOT NULL
	,PRIMARY KEY (id)
);
*/

-- select only users if they are delevopers 
-- SELECT * FROM users u WHERE u.is_developer = 1;

--  insert xiaomi, apple, samsung to companies
/*
INSERT INTO phone_companies (name) VALUES 
	('xiaomi')
	,('apple')
	,('samsung');
*/

-- insert 3 phone (with any data) to phones
/*
INSERT INTO phones (phone_name, company_id, user_id) VALUES 
	('R9', 1, 1)
	,('XS', 2, 3)
	,('A10', 3, 4);
*/

--  write select and save it to file to get phones where company_id=XIAOMI COMPANY ID
-- SELECT * FROM phones p WHERE p.company_id = 1;

-- select all users which have phones
SELECT 
	CONCAT(u.first_name, ' ', u.last_name) AS user_full_name 
FROM 
	users u 
	JOIN phones p ON u.id = p.user_id







