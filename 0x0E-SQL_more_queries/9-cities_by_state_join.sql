-- Write a script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;