-- Write a script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, (SELECT name FROM states
    where id = cities.state_id
) as state_name
FROM citiesORDER BY cities.id ASC;