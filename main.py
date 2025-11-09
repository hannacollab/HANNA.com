#!/usr/bin/env python3
"""
A simple command-line calculator application.
"""

from calculator import Calculator


def print_menu():
    """Print the calculator menu."""
    print("\n" + "=" * 40)
    print("         PYTHON CALCULATOR")
    print("=" * 40)
    print("\nOperations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Power (^)")
    print("  6. Modulo (%)")
    print("  7. Exit")
    print("=" * 40)


def get_number(prompt):
    """Get a number from the user with validation."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    """Main function to run the calculator."""
    calc = Calculator()
    
    print("Welcome to the Python Calculator!")
    
    while True:
        print_menu()
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '7':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("\nInvalid choice! Please select a number between 1 and 7.")
            continue
        
        # Get numbers from user
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        try:
            if choice == '1':
                result = calc.add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}")
            elif choice == '2':
                result = calc.subtract(num1, num2)
                print(f"\nResult: {num1} - {num2} = {result}")
            elif choice == '3':
                result = calc.multiply(num1, num2)
                print(f"\nResult: {num1} * {num2} = {result}")
            elif choice == '4':
                result = calc.divide(num1, num2)
                print(f"\nResult: {num1} / {num2} = {result}")
            elif choice == '5':
                result = calc.power(num1, num2)
                print(f"\nResult: {num1} ^ {num2} = {result}")
            elif choice == '6':
                result = calc.modulo(num1, num2)
                print(f"\nResult: {num1} % {num2} = {result}")
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
