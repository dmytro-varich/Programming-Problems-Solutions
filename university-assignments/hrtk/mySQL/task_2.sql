Use college;

-- TASK 1 - Відобразити прізвища студентів, рік народження яких знаходитися в діапазоні 2000-2002.
SELECT surname_s FROM student
WHERE date_of_birth between '2000-01-01' and '2002-01-01';

-- TASK 2 - Відобразити кількість студентів МОЄЇ ГРУПИ (2).
SELECT COUNT(*) FROM student
WHERE id_gr = 2;

-- TASK 3 - Відобразити назви предметів, які викладаються на третьому курсі.
SELECT subject_name FROM subjects
WHERE course = 3;

-- TASK 4 - Порахувати середній бал для кожного студента.
-- SELECT COUNT(id_st), (mark/2)
-- FROM academic_perfomance_

-- TASK 5 - Відобразити прізвища викладачів комісії Математики.
