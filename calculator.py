"""
A simple calculator module with basic arithmetic operations.
"""


class Calculator:
    """Calculator class for performing basic arithmetic operations."""

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        """Raise a to the power of b."""
        return a ** b

    def modulo(self, a, b):
        """Return the remainder of a divided by b."""
        if b == 0:
            raise ValueError("Cannot perform modulo with zero")
        return a % b
