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
    department ENUM('программування', 'обчислювальна техніка'),
    year_g YEAR,
    n_g tinyint CHECK(1 <= n_g <= 6) 
);

CREATE TABLE subjects (
	id_sub tinyint AUTO_INCREMENT PRIMARY KEY,
    sub_cipher INT NOT NULL,
    subject_name CHAR NOT NULL,
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
