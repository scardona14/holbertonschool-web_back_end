# MySQL Advanced

**By:** Guillaume Plessis, Senior Cloud & System Engineer at WeWork, and Guillaume, CTO at Holberton School  

## Description
This project covers advanced MySQL concepts, designed to improve database design, performance, and management skills.

## Concepts

### Resources
Read or watch:

- [MySQL Cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.mysqltutorial.org/mysql-index/)
- [Stored Procedure](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html)
- [Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/8.0/en/views.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/8.0/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/8.0/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)

---

## Learning Objectives
By the end of this project, you will be able to explain the following to anyone:

### General
- How to create tables with constraints.
- How to optimize queries by adding indexes.
- What stored procedures and functions are and how to implement them in MySQL.
- What views are and how to implement them in MySQL.
- What triggers are and how to implement them in MySQL.

---

## Requirements

### General
- All files will be executed on **Ubuntu 20.04 LTS** using **MySQL 8.0**.
- Each file should end with a new line.
- All SQL queries should have a comment explaining the task above the query.
- Each file should start with a comment describing the task.
- All SQL keywords should be in uppercase (e.g., `SELECT`, `WHERE`).
- A `README.md` file is mandatory in the project root folder.
- File length will be tested using `wc`.

---

## More Info

### Comments for SQL Files

```sql
-- 3 first students in the Batch ID=3 
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;