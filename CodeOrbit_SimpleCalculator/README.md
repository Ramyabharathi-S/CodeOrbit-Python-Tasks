# CodeOrbit_SimpleCalculator

A clean, modular, and beginner-friendly Command Line Interface (CLI) Calculator built with Python for the **CodeOrbit Tech Python Programming Internship**.

---

## 📌 Project Overview
The **Simple Calculator** allows users to perform core arithmetic operations through an interactive terminal interface. It incorporates robust validation, clear modular functions, and comprehensive exception handling for errors such as invalid numeric inputs and division by zero.

---

## 🚀 Features
- **Standard Arithmetic Operations**:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- **Advanced Operations**:
  - Floor Division (`//`)
  - Modulus / Remainder (`%`)
  - Exponentiation / Power (`^`)
- **Robust Error Handling**:
  - Catches `ZeroDivisionError` gracefully with friendly messages.
  - Catches non-numeric inputs using `try...except ValueError` loops.
  - Catches `OverflowError` for massive exponentiations.
- **User-Friendly Interface**:
  - Re-prompts on invalid inputs rather than terminating abruptly.
  - Clean numeric formatting (e.g., outputs `5` instead of `5.0`).
  - Allows multiple calculations per session.

---

## 🛠️ Requirements & Tech Stack
- **Language**: Python 3.8 or newer (tested on Python 3.11)
- **Dependencies**: Standard Library only (`sys`, `math` - no third-party packages required).

---

## 💻 How to Run on Windows

### Option 1: Using VS Code
1. Open Visual Studio Code.
2. Open the folder: `CodeOrbit_SimpleCalculator`.
3. Open `main.py`.
4. Click the **Run Python File** button in the top-right corner, or press `Ctrl + F5`.

### Option 2: Using Windows Terminal / Command Prompt / PowerShell
1. Open PowerShell or Command Prompt.
2. Navigate to the project directory:
   ```powershell
   cd "d:\Badges\CodeOrbit Task\CodeOrbit_SimpleCalculator"
   ```
3. Run the script:
   ```powershell
   python main.py
   ```

---

## 🧪 Test Cases & Sample Output

### Test Case 1: Standard Addition & Division
```text
Select an operation:
  1. Addition (+)
  ...
Enter choice (1-8 or operation symbol): 1
Enter the first number: 45
Enter the second number: 15
-----------------------------------
Result: 45 + 15 = 60
-----------------------------------
```

### Test Case 2: Division by Zero (Exception Handling)
```text
Enter choice (1-8 or operation symbol): 4
Enter the first number: 50
Enter the second number: 0
-----------------------------------
[Math Error] Cannot divide by zero.
-----------------------------------
```

### Test Case 3: Invalid Non-Numeric Input Recovery
```text
Enter choice (1-8 or operation symbol): 3
Enter the first number: abc
[Error] Invalid input. Please enter a valid number (e.g., 10, 3.14).
Enter the first number: 12.5
Enter the second number: 4
-----------------------------------
Result: 12.5 * 4 = 50
-----------------------------------
```

---

## 📚 Code Architecture
- `add()`, `subtract()`, `multiply()`, `divide()`, `floor_divide()`, `modulus()`, `power()`: Pure arithmetic functions that perform isolated calculations.
- `get_number()`: Validates that user input is a valid integer or float.
- `calculate()`: Dispatches the chosen operation with structured exception handling.
- `main()`: Orchestrates the user loop and exit condition.

---

## 👤 Author
Developed for the **CodeOrbit Tech Python Programming Internship**.
