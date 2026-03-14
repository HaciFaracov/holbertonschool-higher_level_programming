-- creates the database hbtn_0d_2 and the user user_0d_2
-- create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant only SELECT privilege on hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
