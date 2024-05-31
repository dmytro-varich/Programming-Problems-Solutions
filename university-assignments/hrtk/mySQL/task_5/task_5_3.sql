use college;

-- Commad: "UPDATE" - GRANTED
UPDATE group_
SET department = 'Програмної інженерії'
WHERE id_gr = 2;

-- Commad: "SELECT" - GRANTED/CHECKING THIS TABLE WITH NEW UPDATES
SELECT * 
FROM group_
WHERE id_gr = 2;

-- Commad: "DROP" - CHECKING: DENIED TO USER 
DROP TABLE IF EXISTS group_;
