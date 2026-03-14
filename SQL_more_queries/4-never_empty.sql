-- creates the table id_not_null with id and name columns
-- create table if not exists
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
