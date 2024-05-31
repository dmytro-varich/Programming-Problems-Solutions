use college; 

-- Commad: "Insert" - GRANTED
Insert into  student (id_st, id_gr, surname_s, sname_, slast_name, date_of_birth, payment, gender_s)
values (16, 2, "Петров", "Владислав", "Костянтинович", "2005-07-25", 'бюджет', 'чоловік');

-- Commad: "SELECT" - GRANTED/CHECKING THIS TABLE WITH NEW UPDATES
SELECT * FROM student;

-- Commad: "CREATE" - CHECKING: DENIED TO USER 
CREATE TABLE test (
	id_tst tinyint AUTO_INCREMENT PRIMARY KEY,
	tname CHAR(30) UNIQUE NOT NULL,
	tmark CHAR(15)
);
