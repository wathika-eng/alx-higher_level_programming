-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT * FROM cities
WHERE state_id = @California_state_id;
ORDER BY id ASC;