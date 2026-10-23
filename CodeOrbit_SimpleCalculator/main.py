"""
CodeOrbit Tech - Python Programming Internship
Project: Simple Calculator
File: main.py
Description: A beginner-friendly, robust CLI calculator supporting basic
             arithmetic, exponentiation, and modulus with comprehensive
             error handling (ZeroDivisionError, ValueError).
"""


def add(num1: float, num2: float) -> float:
    """Return the sum of two numbers."""
    return num1 + num2


def subtract(num1: float, num2: float) -> float:
    """Return the difference between two numbers."""
    return num1 - num2


def multiply(num1: float, num2: float) -> float:
    """Return the product of two numbers."""
    return num1 * num2


def divide(num1: float, num2: float) -> float:
    """
    Return the quotient of two numbers.
    Raises ZeroDivisionError if num2 is zero.
    """
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2


def floor_divide(num1: float, num2: float) -> float:
    """
    Return the integer quotient (floor division) of two numbers.
    Raises ZeroDivisionError if num2 is zero.
    """
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero in floor division.")
    return num1 // num2


def modulus(num1: float, num2: float) -> float:
    """
    Return the remainder of division of two numbers.
    Raises ZeroDivisionError if num2 is zero.
    """
    if num2 == 0:
        raise ZeroDivisionError("Cannot perform modulus by zero.")
    return num1 % num2


def power(num1: float, num2: float) -> float:
    """Return num1 raised to the power of num2."""
    return num1 ** num2


def display_menu():
    """Display the list of supported arithmetic operations."""
    print("\n" + "=" * 45)
    print("      CODEORBIT TECH - SIMPLE CALCULATOR     ")
    print("=" * 45)
    print("Select an operation:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Floor Division (//)")
    print("  6. Modulus (%)")
    print("  7. Exponentiation (^)")
    print("  8. Exit")
    print("=" * 45)


def get_number(prompt: str) -> float:
    """
    Safely prompt the user for numeric input with error handling.
    Loops until a valid float is entered.
    """
    while True:
        raw_val = input(prompt).strip()
        try:
            return float(raw_val)
        except ValueError:
            print("[Error] Invalid input. Please enter a valid number (e.g., 10, 3.14).")


def format_number(num: float) -> str:
    """Format float cleanly: 5.0 -> 5, 5.25 -> 5.25."""
    if num.is_integer():
        return str(int(num))
    return f"{num:.4f}".rstrip("0").rstrip(".")


def calculate(choice: str, a: float, b: float):
    """
    Execute the arithmetic operation based on user choice.
    Returns (result_string, success_boolean).
    """
    try:
        if choice in ("1", "+", "add"):
            res = add(a, b)
            symbol = "+"
        elif choice in ("2", "-", "sub"):
            res = subtract(a, b)
            symbol = "-"
        elif choice in ("3", "*", "mul"):
            res = multiply(a, b)
            symbol = "*"
        elif choice in ("4", "/", "div"):
            res = divide(a, b)
            symbol = "/"
        elif choice in ("5", "//", "floordiv"):
            res = floor_divide(a, b)
            symbol = "//"
        elif choice in ("6", "%", "mod"):
            res = modulus(a, b)
            symbol = "%"
        elif choice in ("7", "^", "**", "pow"):
            res = power(a, b)
            symbol = "^"
        else:
            return "[Error] Unrecognized operation selected.", False

        formatted_result = f"{format_number(a)} {symbol} {format_number(b)} = {format_number(res)}"
        return formatted_result, True

    except ZeroDivisionError as zde:
        return f"[Math Error] {zde}", False
    except OverflowError:
        return "[Math Error] Result is too large to represent (numerical overflow).", False
    except Exception as exc:
        return f"[Unexpected Error] {exc}", False


def main():
    """Main program loop."""
    print("Welcome to CodeOrbit Simple Calculator!")
    
    while True:
        display_menu()
        choice = input("Enter choice (1-8 or operation symbol): ").strip()

        if choice in ("8", "exit", "quit", "q"):
            print("\nThank you for using CodeOrbit Simple Calculator. Goodbye!\n")
            break

        valid_choices = ("1", "2", "3", "4", "5", "6", "7", "+", "-", "*", "/", "//", "%", "^", "**")
        if choice not in valid_choices:
            print("[Error] Invalid selection. Please enter a choice between 1 and 8.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        message, success = calculate(choice, num1, num2)
        print("\n" + "-" * 35)
        if success:
            print(f"Result: {message}")
        else:
            print(message)
        print("-" * 35)

        # Ask if the user wants another calculation
        again = input("\nPerform another calculation? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThank you for using CodeOrbit Simple Calculator. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
