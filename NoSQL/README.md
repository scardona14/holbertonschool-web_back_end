# NoSQL Project

## Resources

Read or watch:

- [NoSQL Databases Explained](https://www.youtube.com/watch?v=O5vzLKg7y-k)
- [What is NoSQL?](https://www.youtube.com/watch?v=ZS_kXvOeQ5Y)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=7CqJlxBYj-M)
- [Aggregation](https://www.mongodb.com/aggregation)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://docs.mongodb.com/manual/reference/method/)
- [The mongo Shell](https://docs.mongodb.com/manual/reference/mongo-shell/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What NoSQL means
- What is the difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are the benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All your files should end with a new line
- The first line of all your files should be a comment: `// my comment`
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using wc
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## More Info

- [Install MongoDB 4.2 in Ubuntu 18.04](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
- [Official installation guide](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
- Potential issue if documents creation doesn’t work or this error: Data directory /data/db not found., terminating (source and source)
- `sudo mkdir -p /data/db` if needed
- Use “container-on-demand” to run MongoDB
- Connect via SSH or via the WebTerminal
- In the container, you should start MongoDB before playing with it:

```bash
$ service mongod start
* Starting database mongod [ OK ]
$ cat 0-list_databases | mongo