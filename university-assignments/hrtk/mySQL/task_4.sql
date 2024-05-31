Use college;

-- TASK 1 - Відобразити рік, назву місяця та кількість студентів вашої групи, що народилися в цьому місяці та році.
SET @row_number = 0;
SELECT (@row_number:=@row_number + 1) as "№", YEAR(date_of_birth) as "Рік", MONTHNAME(date_of_birth) as "Місяць"
FROM student
WHERE MONTH(date_of_birth) = MONTH(NOW())
and YEAR(date_of_birth) = YEAR(NOW())
and id_gr = 2;

-- TASK 2 - Виведіть П.І.Б студентів, що народилися в поточному місяці.
SELECT CONCAT(surname_s, ' ', sname_, ' ', slast_name) as "П.I.Б.", date_of_birth as "Дата" 
FROM student
WHERE MONTH(date_of_birth) = MONTH(NOW());

-- TASK 3 - Скільки мається співробітників кожної статі (чоловіків і жінок)?
SELECT gender_t as "Стать", COUNT(gender_t) as "Кількість" 
FROM teacher 
GROUP BY gender_t;

-- TASK 4 - Знайдіть імена 5 наймолодших студентів вашої групи.
SELECT sname_ as "Ім'я", date_of_birth as "Дата"
FROM student
WHERE id_gr = 2
ORDER BY date_of_birth DESC
LIMIT 5; 

-- TASK 5 - Для однієї з груп виведіть П.І.Б. студента та інформацію про наявність стипендії (якщо середній бал за минулий семестр більше 4).
SELECT CONCAT(surname_s, ' ', sname_) as "Прізвище, ім'я", avg(mark) as "Середній бал", 
IF (avg(mark) >= 4, 'Стипендія', 'немає') as "Наявність Стипендії"
FROM student, academic_perfomance_
WHERE student.id_st=academic_perfomance_.id_st 
GROUP BY 1
