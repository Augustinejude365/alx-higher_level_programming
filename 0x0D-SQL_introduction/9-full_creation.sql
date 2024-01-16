-- A script that creates and fills a table second_table with attributes id, name and score.
CREATE TABLE IF NOT EXISTS second_table (
	    id INT,
	    name VARCHAR(256),
	    score INT
	) ENGINE=INNODB;
	-- Insertion of a row
INSERT INTO second_table
VALUES (1, "John", 10),
       (2, "Alex", 3),
       (3, "Bob", 14),
       (4, "George", 8);
