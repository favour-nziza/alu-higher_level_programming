-- Lists all cities with their state name, sorted by cities.id.
-- Join cities and states
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
