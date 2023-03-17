-- creating second table with values
CREATE TABLE IF NOT EXISTS second_table(
    id INT AUTO_INCREMENT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table VALUES(,'John', 10);
INSERT INTO second_table VALUES(,'Alex', 3);
INSERT INTO second_table VALUES(,'Bob', 14);
INSERT INTO second_table VALUES(,'George', 8);