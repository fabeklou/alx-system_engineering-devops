-- This is the code to create the <tyrell_corp> database,
-- add to it the nexus6 table with one or more records
-- and add CREATE PRIVILEGES to <holberton_user> on the <nexus6> table
CREATE DATABASE IF NOT EXISTS `tyrell_corp`;
USE `tyrell_corp`;
CREATE TABLE IF NOT EXISTS `nexus6` (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO `nexus6` (name, email)
VALUES ('salad', 'salad@food.com'),
    ('tomato', 'tomato@food.com'),
    ('onion', 'onion@food.com');
GRANT SELECT ON `nexus6` TO `holberton_user` @`localhost`;
FLUSH PRIVILEGES;