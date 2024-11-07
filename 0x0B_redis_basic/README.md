# Redis Basic

This project covers the fundamentals of using Redis as a key-value data store and cache. You will learn how to perform basic operations and implement a simple caching mechanism using Redis in Python.

## Project Overview

### Description

In this project, you’ll explore how to use Redis for essential data operations, such as setting and retrieving keys, and utilizing Redis as a simple cache. The project aims to provide practical experience with Redis in a Python environment.

### Learning Objectives
- Understand basic Redis operations and commands
- Implement caching strategies with Redis in Python

## Requirements

- All files are interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.9**
- Each file must end with a new line
- `README.md` at the root of the project directory is mandatory
- All Python files should start with the line `#!/usr/bin/env python3`
- Code should follow **pycodestyle** standards (version 2.5)
- Modules, classes, and functions must have descriptive documentation
  - Example: `python3 -c 'print(__import__("my_module").__doc__)'`
  - Documentation should fully explain the purpose of the module, class, or method
- All functions and coroutines must be type-annotated

### Installation

To install Redis and set up the environment:

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf