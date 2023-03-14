-- Write a script that creates the table id_not_null on your MySQL server.
CREATE TABLE id_not_null IF NOT EXISTS (
    id int,
    name VARCHAR(256)
);