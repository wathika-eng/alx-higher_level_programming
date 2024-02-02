-- Identify duplicate rows in the cities table and keep the one with the lowest id
use hbtn_0e_4_usa;
CREATE TEMPORARY TABLE TempCities AS
SELECT state_id, name, MIN(id) AS min_id
FROM cities
GROUP BY state_id, name
HAVING COUNT(*) > 1;

-- Delete duplicate rows in the cities table
DELETE c FROM cities c
JOIN TempCities tc ON c.state_id = tc.state_id AND c.name = tc.name AND c.id > tc.min_id;

-- Now, you can delete duplicates in the states table
WITH DuplicateCTE AS (
    SELECT 
        name,
        ROW_NUMBER() OVER (PARTITION BY name ORDER BY id) AS row_num
    FROM 
        states
)
DELETE s FROM states s
JOIN DuplicateCTE d ON s.name = d.name AND s.id > d.row_num;

