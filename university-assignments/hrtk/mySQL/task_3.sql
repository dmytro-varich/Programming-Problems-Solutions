Use college;

-- TASK 1 - Відобразити рік, назву місяця та кількість студентів вашої групи, що народилися в цьому місяці та році.
SET @row_number = 0;
SELECT (@row_number:=@row_number + 1) as "№", YEAR(date_of_birth) as "Рік", MONTHNAME(date_of_birth) as "Місяць"
FROM student
WHERE MONTH(date_of_birth) = MONTH(NOW())
and YEAR(date_of_birth) = YEAR(NOW())
and id_gr = 2;

-- TASK 2 - Виведіть П.І.Б студентів, що народилися в поточному місяці.
SELECT surname_s as "Прізвище", sname_ as "Ім'я", slast_name as "по Батькові", date_of_birth as "Дата" 
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
ORDER BY date_of_birth
LIMIT 5; 
