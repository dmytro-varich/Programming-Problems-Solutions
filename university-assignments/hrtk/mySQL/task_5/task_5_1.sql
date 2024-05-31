USE mysql; USE college;

-- TASK 1 - створити 4 облікових записів нових користувачів і наділити їх різними привілеями відносно різних таблиць (3-4 привілеї для кожного користувача);

-- USER_1
DROP USER IF EXISTS 'Varich1'@'localhost';
CREATE USER 'Varich1'@'localhost' IDENTIFIED BY '1234';
GRANT SELECT, INSERT, DELETE, DROP ON college.student TO 'Varich1'@'localhost';
FLUSH PRIVILEGES;

-- USER_2
DROP USER IF EXISTS 'Varich2'@'localhost';
CREATE USER 'Varich2'@'localhost' IDENTIFIED BY '1234';
GRANT SELECT, UPDATE, CREATE ON college.group_ TO 'Varich2'@'localhost';
FLUSH PRIVILEGES;
	
-- USER_3
DROP USER IF EXISTS 'Varich3'@'localhost';
CREATE USER 'Varich3'@'localhost' IDENTIFIED BY '1234';
GRANT ALTER, CREATE, INSERT, SELECT ON college.teacher TO 'Varich3'@'localhost';
FLUSH PRIVILEGES;

-- USER_4
DROP USER IF EXISTS 'Varich4'@'localhost';
CREATE USER 'Varich4'@'localhost' IDENTIFIED BY '1234';
GRANT ALL ON *.* TO 'Varich4'@'localhost'; 
FLUSH PRIVILEGES;
