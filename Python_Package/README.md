# Creating a Python Package – mymath

## Overview

This project demonstrates how to create a custom Python package named **mymath**, composed of multiple modules that implement reusable mathematical functions.

The package includes:

* basic arithmetic functions
* statistical calculations
* geometry utilities

This lab reinforces modular programming concepts and package structuring in Python, which are essential for building scalable and reusable code in data engineering workflows.

---

## Project Structure

```
mymath/
│
├── __init__.py
├── basic.py
├── stats.py
├── geometry.py
```

---

## Modules and Functions

### basic module

Includes fundamental arithmetic operations:

* `square(number)` → returns the square of a number
* `double(number)` → returns twice the value
* `add(a, b)` → returns the sum of two numbers

Example:

```python
mymath.basic.square(4)
Output: 16
```

---

### stats module

Includes statistical calculations:

* `mean(numbers)` → returns the average value
* `median(numbers)` → returns the middle value

Example:

```python
mymath.stats.mean([3,4,5])
Output: 4.0
```

---

### geometry module

Includes geometry utility functions:

* `area_of_rectangle(length, breadth)`
* `area_of_circle(radius)`

Example:

```python
mymath.geometry.area_of_rectangle(5,4)
Output: 20
```

```python
mymath.geometry.area_of_circle(5)
Output: 78.5
```

---

## How to Run the Package

Open a terminal and start Python:

```
python3
```

Import the package:

```
import mymath
```

Run example tests:

```
mymath.basic.add(3,4)
mymath.stats.mean([3,4,5])
mymath.geometry.area_of_circle(5)
```

If the commands execute successfully, the package is working correctly.

---

## Skills Demonstrated

This project demonstrates:

* creating Python modules
* structuring a Python package
* using `__init__.py`
* organizing reusable functions
* importing modules from a package
* verifying functionality through interpreter testing

These skills are essential for developing maintainable Python code in data engineering environments.

---
