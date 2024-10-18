# User Authentication Service

## Description
This project involves implementing a user authentication service using Flask. In real-world applications, you should **not** implement your own authentication system, but use a well-established module or framework (e.g., Flask-User in Python-Flask). However, for the purpose of learning, we will walk through each step to understand how authentication mechanisms work by implementing them ourselves.

## Resources
Here are some resources that will help you through this project:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Requests Module Documentation](https://docs.python-requests.org/en/latest/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Learning Objectives
By the end of this project, you should be able to explain:
- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- You should use SQLAlchemy for the database interaction
- All your files must be executable
- The length of your files will be tested using `wc`

### Documentation
- All your modules should have documentation (use `python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (use `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation:
  - `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
  - `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
  
  The documentation should clearly explain the purpose of the module, class, or method in full sentences, and the length will be verified.
- All your functions should be type annotated

### Flask App Requirements
- The Flask app should only interact with the `Auth` class and never directly with the `DB` class.
- Only public methods of the `Auth` and `DB` classes should be used outside these classes.

## Setup

### Installing `bcrypt`
You will need to install the `bcrypt` library for handling password hashing and checking:
```bash
pip3 install bcrypt