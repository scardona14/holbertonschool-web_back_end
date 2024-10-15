# Session Authentication

## Description
In this project, you will implement a Session Authentication system from scratch. Note that in a real-world industry environment, you should **not** implement your own Session authentication system. Instead, you should use an existing module or framework that handles this for you (e.g., Flask-HTTPAuth in Python). However, for the purposes of learning, we will go through each step of the mechanism to understand how it works.

## Resources
Here are some resources to help you better understand session authentication:

- [REST API Authentication Mechanisms](#) (Focus on the session auth part)
- [HTTP Cookies](#)
- [Flask Documentation](#)
- [Flask Cookie Documentation](#)

## Learning Objectives
By the end of this project, you should be able to explain the following concepts:

### General:
- What authentication means
- What session authentication means
- What cookies are
- How to send cookies
- How to parse cookies

## Requirements

### Python Scripts:
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9
- All files must end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Code must follow the `pycodestyle` style guide (version 2.5)
- All files must be executable
- File lengths will be tested using `wc`
  
### Documentation:
- All modules should include documentation (use `python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should include documentation (use `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should include documentation:
  - `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
  - `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
  
  The documentation should be more than just a simple word; it should be a full sentence that explains the purpose of the module, class, or function (the length will be verified).
