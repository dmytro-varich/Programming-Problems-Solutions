drop database if exists college;
CREATE DATABASE college;
Use college;

CREATE TABLE chair (
	id_ch tinyint AUTO_INCREMENT PRIMARY KEY,
	cname CHAR(30) UNIQUE NOT NULL,
	cphone CHAR(15)
);

CREATE TABLE group_ (
	id_gr tinyint AUTO_INCREMENT PRIMARY KEY,
    gname CHAR(2),
    course CHAR(1),
    department ENUM('Програмної інженерії', "Комп'ютерної інженерії"),
    year_g YEAR,
    n_g tinyint CHECK(1 <= n_g <= 6) 
);

CREATE TABLE subjects (
	id_sub tinyint AUTO_INCREMENT PRIMARY KEY,
    sub_cipher INT NOT NULL,
    subject_name CHAR(40) NOT NULL,
    total_hours INT,
    lectures INT,
    laboratory INT,
    semester INT CHECK(1 <= semester <= 8),
    type_of_offset ENUM('залік', 'екзамен')
);

CREATE TABLE teacher(
	id_t INT AUTO_INCREMENT PRIMARY KEY,
	full_name_t CHAR(40) NOT NULL,
    id_ch TINYINT,
	category ENUM("1", "2", "вища", "методист"),
	gender_t ENUM('чоловік','жінка'), 
    FOREIGN KEY (id_ch)
		REFERENCES chair (id_ch)
);

CREATE TABLE student (
	id_st TINYINT AUTO_INCREMENT PRIMARY KEY,
	id_gr TINYINT,
	surname_s CHAR(40) NOT NULL,
	sname_ CHAR(40) NOT NULL,
	date_of_birth DATE,
	payment ENUM ('бюджет','контракт'),
	gender_s ENUM('чоловік','жінка'),
	FOREIGN KEY (id_gr) 
		REFERENCES group_(id_gr)
);

CREATE TABLE DISTRIBUTION(
	id_d int AUTO_INCREMENT PRIMARY KEY,
    id_sub TINYINT,
    id_t INT,
	date_certification DATE,
	academic_year YEAR,
	FOREIGN KEY (id_sub) 
		REFERENCES subjects(id_sub),
	FOREIGN KEY (id_t) 
		REFERENCES teacher(id_t)
);

CREATE TABLE academic_perfomance_(
	id_ap int AUTO_INCREMENT PRIMARY KEY,
    id_st TINYINT,
    id_d INT,
	mark INT CHECK(2 <= mark <= 5),
	FOREIGN KEY (id_st) 
		REFERENCES student(id_st),
	FOREIGN KEY (id_d) 
		REFERENCES DISTRIBUTION(id_d)
);

Insert into chair (id_ch, cname, cphone)
values (1, 'Математики', '234'),
	   (2, "Мов та літератури", '235'), 
	   (3, "Фізичного виховання", '236'),
       (4, "Програмної інженерії", '237'),
       (5, "Комп'ютерної інженерії", '238');

Insert into group_ (id_gr, gname, course, n_g, year_g, department)
values (1, 'П', '1', 1, 2019, "Програмної інженерії"),
	   (2, 'Е', '1', 2, 2019, "Комп'ютерної інженерії"), 
	   (3, 'П', '2', 1, 2018, "Програмної інженерії"),
       (4, 'Е', '2', 2, 2018, "Комп'ютерної інженерії"),
       (5, 'П', '3', 1, 2017, "Програмної інженерії"),
       (6, 'Е', '3', 4, 2017, "Комп'ютерної інженерії"),
       (7, 'Е', '3', 5, 2017, "Комп'ютерної інженерії"),
       (8, 'П', '4', 1, 2016, "Програмної інженерії"),
	   (9, 'Е', '4', 1, 2016, "Комп'ютерної інженерії");
       
Insert into subjects (id_sub, sub_cipher, subject_name, total_hours, lectures, laboratory, semester, type_of_offset)
values (1, 234, "Математика", 135, 60, 0, 1, 'Залік'),
	   (2, 234, 'Математика', 145, 80, 0, 2, 'Екзамен'), 
	   (3, 236, "Архітектура ПК", 125, 48, 20, 3, 'Залік'),
       (4, 238, 'Програмування', 165, 68, 16, 3, 'Залік'),
       (5, 238, 'Програмування', 165, 60, 20, 4, 'Екзамен'),
       (6, 239, 'ООП', 108, 48, 16, 4, 'Залік'),
       (7, 239, 'ООП', 161, 68, 24, 5, 'Екзамен'),
       (8, 240, "Комп'ютерні мережи", 108, 56, 10, 6, 'Залік'),
	   (9, 240, "Комп'ютерні мережи", 125, 68, 16, 7, 'Екзамен'),
       (10, 241, "Бази даних", 81,  48, 12, 6, 'Залік'),
       (11, 242, 'Веб-Технології', 108, 40, 16, 6, 'Залік'),
       (12, 242, 'Веб-Технології', 108, 42, 16, 7, 'Екзамен');
       
       
Insert into  teacher (id_t, full_name_t, category, id_ch, gender_t)
values (1, "Батирєва Т.І.", "вища", 1, 'жінка'),
	   (2, "Корнілова Т.І", "вища", 1, 'жінка' ), 
	   (3, "Грищенко О.І", "методист", 3, 'чоловік'),
       (4, "Кулік Ю.В.", "1", 4, 'чоловік'),
       (5, "Ахмедзянова А.О.", "вища", 4, 'жінка'),
       (6, "Мальцева Т.І.", "2", 4, 'жінка'),
       (7, "Жадченко М.П.", "1", 5, 'чоловік'),
       (8, "Жадченко І.Ю.", "1", 5, 'жінка');

Insert into  student (id_st, id_gr, surname_s, sname_, date_of_birth, payment, gender_s)
values (1, 1, "Покотило", "Мирослава", "2003-09-12", 'бюджет', 'жінка'),
	   (2, 1, "Іваненко", "Іван", "2003-01-12", 'бюджет', 'чоловік'), 
	   (3, 1, "Височанський", "Матвій", "2004-01-23", 'контракт', 'чоловік'),
       (4, 3, "Батюк", "Артем", "2002-07-07", 'бюджет', 'чоловік'),
       (5, 3, "Остапенко", "Регіна", "2002-07-07", 'бюджет', 'жінка'),
       (6, 4, "Боярчук", "Аліса", "2001-09-23", 'контракт', 'жінка'),
       (7, 5, "Стоцький", "Дмитро", "2001-12-12", 'контракт', 'чоловік'),
       (8, 5, "Сердюк", "Михайло", "2001-05-23", 'контракт', 'чоловік'),
	   (9, 6, "Юрченко", "Світлана", "2000-05-24", 'бюджет', 'жінка'),
	   (10, 2, "Варіч", "Дмитро", "2004-06-07", 'бюджет', 'чоловік'), 
       (11, 2, "Поляков", "Роман", "2003-05-26", 'бюджет', 'чоловік'),
       (12, 2, "Рагулін", "Антон", "2004-11-07", 'бюджет', 'чоловік'),
       (13, 6, "Лавренова", "Діана", "2004-04-21", 'бюджет', 'жінка');

Insert into  DISTRIBUTION (id_d, id_sub, id_t, date_certification, academic_year)
values (1, 1, 1, "2019-12-20", 2019),
	   (2, 3, 3, "2019-12-23", 2019), 
	   (3, 4, 6, "2019-12-28", 2019),
       (4, 6, 2, "2020-12-19", 2020),
	   (5, 8, 4, "2020-12-21", 2020), 
	   (6, 10, 5, "2020-12-26", 2020),
       (7, 2, 8, "2021-09-21", 2021),
	   (8, 3, 3, "2021-01-25", 2021), 
	   (9, 5, 7, "2021-01-29", 2021);
       
Insert into academic_perfomance_ (id_ap, id_st, id_d, mark)
values (1, 10, 1, 3), 
	   (2, 10, 2, 4),
       (3, 10, 3, 4),
       (4, 10, 4, 5),
       (5, 10, 5, 4),
       (6, 10, 6, 3),
       (7, 10, 7, 5),
       (8, 10, 8, 3),
       (9, 10, 9, 4),
       (10, 11, 1, 5),
       (11, 11, 2, 4),
       (12, 11, 3, 3),
       (13, 11, 4, 3),
       (14, 11, 5, 4),
       (15, 11, 6, 4),
       (16, 11, 7, 5),
       (17, 11, 8, 3),
       (18, 11, 9, 4),
       (19, 12, 1, 5),
       (20, 12, 2, 5),
       (21, 12, 3, 4),
       (22, 12, 4, 4),
       (23, 12, 5, 3),
       (24, 12, 6, 4),
       (25, 12, 7, 3),
       (26, 12, 8, 5),
       (27, 12, 9, 5),
       (28, 13, 1, 5),
       (29, 13, 2, 5),
       (30, 13, 3, 4),
       (31, 13, 4, 5),
       (32, 13, 5, 4),
       (33, 13, 6, 5),
       (34, 13, 7, 5),
       (35, 13, 8, 3),
       (36, 13, 9, 5);    
