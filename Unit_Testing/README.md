# Unit Testing Lab -- Python (unittest)

## Overview

This project contains **two unit testing activities** implemented using
Python's built‑in `unittest` framework.\
The objective is to demonstrate how to create functions and validate
them using structured automated tests.

This lab follows a modular testing approach where each functional script
has its corresponding test file.

------------------------------------------------------------------------

## Project Structure

    unit-testing-lab/
    │
    ├── mymodule.py
    ├── test_mymodule.py
    │
    ├── activity.py
    └── test_activity.py

Each module contains application logic, and each test file validates
that logic using unit tests.

------------------------------------------------------------------------

# Activity 1 -- Testing square() and double()

## File: `mymodule.py`

Contains two functions:

### square(number)

Returns the square of a number

Example:

    square(2) → 4
    square(3.0) → 9.0
    square(-3) → 9

------------------------------------------------------------------------

### double(number)

Returns twice the value of a number

Example:

    double(2) → 4
    double(-3.1) → -6.2
    double(0) → 0

------------------------------------------------------------------------

## File: `test_mymodule.py`

Tests implemented:

    square(2) == 4
    square(3.0) == 9.0
    square(-3) != -9

    double(2) == 4
    double(-3.1) == -6.2
    double(0) == 0

Concepts used:

-   assertEqual
-   assertNotEqual
-   TestCase class structure
-   automatic test discovery

------------------------------------------------------------------------

# Activity 2 -- Testing add()

## File: `activity.py`

Contains:

### add(a, b)

Returns the sum of two values

Examples:

    add(2,4) → 6
    add(0,0) → 0
    add(2.3,3.6) → 5.9
    add("hello","world") → "helloworld"

------------------------------------------------------------------------

## File: `test_activity.py`

Tests implemented:

    add(2,4) == 6
    add(0,0) == 0
    add(2.3,3.6) == 5.9
    add("hello","world") == "helloworld"
    add(2.3000,4.300) == 6.6
    add(-2,-2) != 0

Concepts used:

-   numeric validation
-   float precision validation
-   string concatenation testing
-   edge‑case validation
-   negative condition testing using assertNotEqual

------------------------------------------------------------------------

# How to Run the Tests

Run Activity 1 tests:

    python3 test_mymodule.py

Run Activity 2 tests:

    python3 test_activity.py

------------------------------------------------------------------------

# Expected Output

If tests pass successfully:

    OK

If any test fails:

    FAILED

Python will display which test failed and why.

------------------------------------------------------------------------

# Testing Concepts Demonstrated

  Concept           Description
  ----------------- -----------------------------------------
  TestCase          Groups related tests
  assertEqual       Validates expected results
  assertNotEqual    Validates incorrect results are avoided
  test\_ prefix     Enables automatic test discovery
  unittest.main()   Executes all test cases

------------------------------------------------------------------------

# Skills Demonstrated

This project demonstrates:

-   writing modular Python functions
-   creating structured unit tests
-   validating multiple data types
-   testing edge cases
-   organizing test files professionally
-   executing automated test suites

------------------------------------------------------------------------

# Author

Unit Testing Lab completed as part of Python testing practice using
unittest framework.
