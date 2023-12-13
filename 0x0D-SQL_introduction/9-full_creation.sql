-- Create a full table
USE hbtn_0c_0

CREATE TABLE IF NOT EXISTS ```second_table```(```id``` INT,```name``` VARCHAR(256), ```score``` INT);

INSTER INTO ```second_table``` VALUES (id,name,score) ( 
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8),
);
