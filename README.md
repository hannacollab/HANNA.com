# HANNA.com

## Python Calculator

A simple command-line calculator built with Python that supports basic arithmetic operations.

### Features

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Power (^)
- Modulo (%)
- Input validation and error handling
- Interactive menu-driven interface

### Usage

To use the calculator, run the main script:

```bash
python3 main.py
```

The calculator will display an interactive menu where you can:
1. Select an operation (1-6)
2. Enter two numbers
3. View the result
4. Continue with more calculations or exit (option 7)

### Example

```
Welcome to the Python Calculator!

========================================
         PYTHON CALCULATOR
========================================

Operations:
  1. Addition (+)
  2. Subtraction (-)
  3. Multiplication (*)
  4. Division (/)
  5. Power (^)
  6. Modulo (%)
  7. Exit
========================================

Enter your choice (1-7): 1
Enter first number: 5
Enter second number: 3

Result: 5.0 + 3.0 = 8.0
```

### Module Usage

You can also import and use the calculator module directly in your Python code:

```python
from calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)      # Returns 8
result = calc.divide(10, 2)  # Returns 5.0
```

### Error Handling

The calculator includes error handling for:
- Division by zero
- Modulo by zero
- Invalid input (non-numeric values)