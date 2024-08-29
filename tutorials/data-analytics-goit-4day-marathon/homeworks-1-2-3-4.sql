SELECT country_name, term region_name, refresh_date, rank, score, week 
FROM bigquery-public-data.google_trends.international_top_terms
LIMIT 100;


SELECT term region_name, refresh_date, rank, score, week 
FROM bigquery-public-data.google_trends.top_terms
LIMIT 100;


-- Вправа №1: Надати для вашого регіону ТОП-25 запитів за минулий тиждень
SELECT term
FROM bigquery-public-data.google_trends.international_top_terms
WHERE country_name = "Ukraine"
AND refresh_date = '2024-08-20'
AND region_name = "Kharkiv Oblast"
AND week = '2024-08-18'
ORDER BY rank
LIMIT 25; 


-- Вправа №2: Відпрацювання максимальної дати/тижня
SELECT MAX(week) AS max_week, MAX(refresh_date) AS max_date
FROM bigquery-public-data.google_trends.international_top_terms;


-- Вправа №2: Обрати свій регіон
SELECT DISTINCT region_name
FROM bigquery-public-data.google_trends.international_top_terms
WHERE country_name = "Ukraine";


SELECT DISTINCT term, country_name, rank, score, refresh_date
FROM bigquery-public-data.google_trends.international_top_terms
WHERE refresh_date = '2024-08-20'
AND term LIKE "%2024%"
LIMIT 100;


SELECT * 
FROM bigquery-public-data.google_trends.international_top_terms
WHERE country_name = "Ukraine"
AND refresh_date >= '2024-08-20'
AND week BETWEEN '2024-01-01' AND CURRENT_DATE()
ORDER BY rank;
