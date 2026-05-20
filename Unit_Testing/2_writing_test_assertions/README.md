# Stack Unit Testing with Nose

Implementation of a simple `Stack` data structure in Python along with unit tests using `nose` and assertions.

This exercise focuses on:
- Writing unit tests
- Using assertions effectively
- Testing stack operations
- Running tests with `nosetests`

---

## 📂 Project Structure

```bash
.
├── stack.py              # Stack implementation
├── test_stack.py         # Unit tests
├── requirements.txt      # Python dependencies
└── setup.cfg             # Nose test configuration
```

---

## 🚀 Features

The `Stack` class includes the following methods:

- `push()` → Adds an item to the top of the stack
- `pop()` → Removes and returns the top item
- `peek()` → Returns the top item without removing it
- `is_empty()` → Checks whether the stack is empty

---

## 🧪 Unit Testing

The project uses `nose` for automated testing.

Implemented test cases:
- Test empty stack behavior
- Test push operation
- Test pop operation
- Test peek operation

Assertions used:
- `assertTrue`
- `assertFalse`
- `assertEqual`

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <repository-name>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests

Run all tests:

```bash
nosetests
```

Run tests and stop at the first failure:

```bash
nosetests --stop
```

---

## 🛠️ Technologies Used

- Python
- Nose
- Unit Testing
- Assertions

---

## 📘 Learning Objectives

Through this exercise I practiced:
- Writing test assertions
- Validating expected outputs
- Testing data structures
- Improving code reliability through automated testing

---
