```markdown
# 0x14 MySQL

This project demonstrates the creation of MySQL users, granting privileges, and setting up replication. The SQL script is divided into three tasks, each with its own set of comments explaining the purpose and functionality of the SQL statements.

## Prerequisites

- MySQL server installed and running
- Access to the MySQL server with appropriate permissions


## Tasks

### Task 1: Create a User and Grant Replication Client Privilege

```sql
-- CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
-- This statement creates a new MySQL user account named 'holberton_user' with the specified password 'projectcorrection280hbtn'.
-- The user can only connect from the local machine (localhost).

CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
-- This statement grants the 'REPLICATION CLIENT' privilege to the 'holberton_user' user.
-- This privilege is required for the user to connect to the replication master and retrieve binary log events for replication purposes.

GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
```

### Task 2: Create a Database, Table, and Grant Privileges

```sql
-- CREATE DATABASE tyrell_corp;
-- This statement creates a new database named 'tyrell_corp'.

CREATE DATABASE tyrell_corp;

-- USE tyrell_corp;
-- This statement selects the 'tyrell_corp' database as the current database for subsequent operations.

USE tyrell_corp;

-- CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));
-- This statement creates a new table named 'nexus6' within the 'tyrell_corp' database.
-- The table has two columns: 'id' (an auto-incrementing integer primary key) and 'name' (a VARCHAR string with a maximum length of 255 characters).

CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));

-- INSERT INTO nexus6 (name) VALUES ('Leon');
-- This statement inserts a new row into the 'nexus6' table with the value 'Leon' in the 'name' column.

INSERT INTO nexus6 (name) VALUES ('Leon');

-- GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
-- This statement grants the 'SELECT' privilege to the 'holberton_user' user on the 'nexus6' table within the 'tyrell_corp' database.
-- This allows the user to read data from the table.

GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
```

### Task 3: Create a Replication User and Grant Privileges

```sql
-- CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_user';
-- This statement creates a new MySQL user account named 'replica_user' with the password 'replica_user'.
-- The '%' wildcard means that the user can connect from any host.

CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_user';

-- GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
-- This statement grants the 'REPLICATION SLAVE' privilege to the 'replica_user' user.
-- This privilege is required for the user to connect to the replication master and act as a replication slave.

GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
-- This statement grants the 'SELECT' privilege to the 'holberton_user' user on the 'mysql.user' table.
-- This table contains information about MySQL user accounts, and granting this privilege allows the user to read user account information.

GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
```

By executing this SQL script, you will create two MySQL user accounts ('holberton_user' and 'replica_user'), grant necessary privileges for replication and data access, create a database and table, and populate the table with sample data.

## Additional Resources

- [MySQL User Account Management](https://dev.mysql.com/doc/refman/8.0/en/user-account-management.html)
- [MySQL Replication](https://dev.mysql.com/doc/refman/8.0/en/replication.html)
- [MySQL Privileges](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html)

```