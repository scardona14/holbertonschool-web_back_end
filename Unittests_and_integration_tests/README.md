# Unittests and Integration Tests

## Overview

This project focuses on implementing **unit tests** and **integration tests** to ensure code reliability and accuracy in various scenarios. Unit tests validate isolated functions, while integration tests verify end-to-end functionality across components. You will apply techniques like **mocking**, **parameterization**, and **fixtures** to create efficient and reusable test cases.

## Objectives

By completing this project, you will:
- Understand and differentiate between unit and integration tests.
- Implement tests that follow best practices using the `unittest` framework.
- Use key testing patterns, including mocking, parameterization, and fixtures.

## Requirements

- **Python version**: 3.9 (Ubuntu 20.04 LTS)
- **Coding style**: `pycodestyle` (version 2.5)
- **Documentation**: All modules, classes, and functions must have descriptive documentation.
- **Type Annotations**: All functions and coroutines must be type-annotated.
- **Execution**: Ensure all files are executable.

## Project Structure

This project includes the following key files:

- **utils.py**: Contains utility functions to be unit tested.
- **client.py**: Implements `GithubOrgClient`, which interacts with the GitHub API.
- **fixtures.py**: Includes example data for integration tests.
- **test_utils.py**: Contains unit tests for `utils.py`.
- **test_client.py**: Contains unit and integration tests for `client.py`.

## Running Tests

Run tests with:
```bash
$ python -m unittest path/to/test_file.py