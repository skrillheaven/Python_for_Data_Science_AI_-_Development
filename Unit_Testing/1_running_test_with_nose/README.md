
# Running Unit Tests with Nose

## 📌 Overview
This practice demonstrates how to run Python unit tests using `unittest` and `nose`, add colorful test output with `pinocchio`, and generate coverage reports with `coverage`.

---

# 📦 Required Libraries

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
python3.8 -m pip install nose
python3.8 -m pip install pinocchio
python3.8 -m pip install coverage
```

### 🔹 Purpose of each package
- `nose` → Test runner for executing unit tests
- `pinocchio` → Adds colorful and readable test output
- `coverage` → Measures how much code is covered by tests

---

# ▶ Running Tests

## Run tests with unittest

```bash
python3 -m unittest
```

## Run tests with verbose output

```bash
python3 -m unittest -v
```

## Run tests with Nose

```bash
nosetests -v
```

---

# 🎨 Add Colored Output with Pinocchio

```bash
nosetests --with-spec --spec-color
```

### Features
- Better readability
- Colorized output
- Spec-style formatting

---

# 📊 Generate Coverage Reports

Run tests with coverage enabled:

```bash
nosetests --with-spec --spec-color --with-coverage
```

Generate a detailed missing-line coverage report:

```bash
coverage report -m
```

---

# ⚙ Automating Test Configuration with `setup.cfg`

Instead of typing all parameters every time, create a `setup.cfg` file.

## Example `setup.cfg`

```ini
[nosetests]
verbosity=2
with-spec=1
spec-color=1
with-coverage=1
cover-erase=1
cover-package=triangle

[coverage:report]
show_missing = True
```

---

# 🚀 Run Tests Using Configuration File

Once `setup.cfg` exists, simply run:

```bash
nosetests
```

All configurations will be applied automatically.

---

# 📂 Project Structure

```bash
project/
│
├── README.md
├── requirements.txt
├── setup.cfg
├── triangle.py
├── test_triangle.py
└── .gitignore
```

---

# ✅ Topics Practiced

- Python unit testing
- Running tests with Nose
- Coverage analysis
- Test output formatting
- Test automation with configuration files

---

# 🧠 Key Takeaway

Using `nose`, `pinocchio`, and `coverage` together improves test readability and helps maintain high-quality Python applications with better visibility into test execution and code coverage.