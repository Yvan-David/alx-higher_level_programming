-- script that creates DB and User with some privileges on the DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
USE hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2 .* TO 'user_0d_2'@'localhost';