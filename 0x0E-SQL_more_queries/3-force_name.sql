-- Write a script that creates the table force_name 
-- on your MySQL server.
CREATE TABLE IF NOT EXISTS force_name (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);
