Use college;

-- TASK 1 - Відобразити прізвища студентів, рік народження яких знаходитися в діапазоні 2000-2002.
SELECT surname_s as "Прізвище" FROM student
WHERE date_of_birth between '2000-01-01' and '2002-01-01';

-- TASK 2 - Відобразити кількість студентів МОЄЇ ГРУПИ (2).
SELECT COUNT(*) as "COUNT" FROM student
WHERE id_gr = 2;

-- TASK 3 - Відобразити назви предметів, які викладаються на третьому курсі.
SELECT subjects.subject_name as 'Назва предмету', group_.course as 'Курс'
FROM subjects, group_, DISTRIBUTION, student, academic_perfomance_
WHERE group_.id_gr=student.id_gr
and student.id_st=academic_perfomance_.id_st 
and academic_perfomance_.id_d=DISTRIBUTION.id_d
and DISTRIBUTION.id_sub=subjects.id_sub
and group_.course=3 
GROUP BY 1;

-- TASK 4 - Порахувати середній бал для кожного студента.
SELECT CONCAT(surname_s, ' ', sname_) as "Прізвище, ім'я", avg(mark) as "Середній бал"
FROM student, academic_perfomance_
WHERE student.id_st=academic_perfomance_.id_st
GROUP BY 1;

-- TASK 5 - Відобразити прізвища викладачів комісії Математики.
SELECT full_name_t as 'Прізвища'
FROM chair, teacher
WHERE chair.id_ch=teacher.id_ch
and cname='Математики'
