-- This is the code to create a new user for the replica server
-- https: // dev.mysql.com / doc / refman / 5.7 / en / replication - howto - repuser.html
CREATE USER 'replica_user' @'%' IDENTIFIED BY 'full_belly_42';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user' @'%';
GRANT SELECT ON mysql.user TO 'holberton_user' @'localhost';