use college;

-- Commad: "CREATE" - GRANTED
CREATE TABLE test (
	id_tst tinyint AUTO_INCREMENT PRIMARY KEY,
	test_name CHAR(30) UNIQUE NOT NULL,
	test_mark CHAR(15)
);

-- Commad: "INSERT" - GRANTED
Insert into test (id_tst, test_name, test_mark)
values (1, 'Ukraine', '234'),
	   (2, "USA", '235'), 
	   (3, "United Kingdom", '236');
       
-- Commad: "SELECT" - GRANTED	
SELECT * FROM test;
