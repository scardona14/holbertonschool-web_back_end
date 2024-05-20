# ES6 Data Manipulation

## Project Overview

This project focuses on data manipulation using ES6 features such as map, filter, reduce, typed arrays, and various data structures like Set, Map, and WeakMap.

## Learning Objectives

By the end of this project, you should be able to explain the following without using Google:
- How to use `map`, `filter`, and `reduce` on arrays.
- Typed arrays.
- The Set, Map, and WeakMap data structures.

## Requirements

- All files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x.
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Use the `.js` extension for your code files.
- Code will be tested using Jest and the command `npm run test`.
- Code will be verified against lint using ESLint.
- Code must pass all tests and lint. Verify the entire project by running `npm run full-test`.
- All functions must be exported.

## Setup

### Install NodeJS 12.11.x

In your home directory, run the following commands:
```bash
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v # should output v12.11.1
npm -v # should output 6.11.3