-- Lists all the cities of California in the database hbtn_0d_usa (no JOIN).
-- Select cities using a subquery
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
