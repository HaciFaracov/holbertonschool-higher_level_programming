-- creates the database hbtn_0d_usa and the table states
-- create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the database
USE hbtn_0d_usa;
-- create table states if not exists
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
