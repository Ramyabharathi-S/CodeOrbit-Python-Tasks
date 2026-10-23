# CodeOrbit Tech — Python Programming Internship Portfolio

Welcome to the **CodeOrbit Tech Python Programming Internship** submission repository. This repository contains the complete implementation of all **6 projects** for the **2 Month Internship Tier**, written in clean, idiomatic, beginner-friendly Python with comprehensive error handling, modular functions, and detailed documentation.

---

## 📁 Repository & Project Structure

Each task is organized in an independent folder strictly adhering to the CodeOrbit naming convention (`CodeOrbit_ProjectName/`):

```text
CodeOrbit Task/
│
├── Python-Programming-Tasks-CodeOrbitTech.pdf   # Official Internship Tasks Specification
├── README.md                                    # Master Repository Overview (This file)
├── SUBMISSION_GUIDE.md                          # Git, LinkedIn, Video Script & Review Guide
│
├── CodeOrbit_SimpleCalculator/                  # Task 1: Simple Calculator
│   ├── main.py                                  # Modular arithmetic logic & exception handling
│   ├── README.md                                # Setup & usage instructions
│   └── sample_output.txt                        # Recorded execution test results
│
├── CodeOrbit_TodoListCLI/                       # Task 2: To-Do List CLI App
│   ├── main.py                                  # CLI menu & list management logic
│   ├── tasks.txt                                # Persistent plain-text storage
│   ├── README.md                                # Setup & usage instructions
│   └── sample_output.txt                        # Recorded execution test results
│
├── CodeOrbit_NumberGuessingGame/                # Task 3: Number Guessing Game
│   ├── main.py                                  # Random generation, hints, and replay loop
│   ├── README.md                                # Setup & usage instructions
│   └── sample_output.txt                        # Recorded execution test results
│
├── CodeOrbit_FileHandlingRecords/               # Task 4: File Handling Mini Project
│   ├── main.py                                  # Student records CRUD manager using CSV
│   ├── records.csv                              # CSV dataset with initial seed records
│   ├── README.md                                # Setup & usage instructions
│   └── sample_output.txt                        # Recorded execution test results
│
├── CodeOrbit_DataStructuresPractice/            # Task 5: Simple Data Structures Practice
│   ├── main.py                                  # 4 core problems (Lists, Dicts, Sets)
│   ├── README.md                                # Setup & problem breakdown
│   └── sample_output.txt                        # Recorded execution test results
│
└── CodeOrbit_FileAutomation/                    # Task 6: Simple Automation Script
    ├── main.py                                  # File categorizer & bulk batch renamer
    ├── automation_log.txt                       # Audit execution log
    ├── README.md                                # Setup & usage instructions
    ├── sample_output.txt                        # Recorded execution test results
    └── test_files/                              # Generated test sandbox directory
```

---

## 🚀 Projects Overview

| # | Project Name | Key Concepts | File Persistence | Error Handling |
|---|--------------|--------------|------------------|----------------|
| **1** | [CodeOrbit_SimpleCalculator](./CodeOrbit_SimpleCalculator/) | Functions, Float conversions, Modulo, Exponentiation | N/A | `ZeroDivisionError`, `ValueError`, `OverflowError` |
| **2** | [CodeOrbit_TodoListCLI](./CodeOrbit_TodoListCLI/) | Lists, Dictionaries, State Flags, Terminal UI | `tasks.txt` (Auto-save) | `IndexError`, `ValueError`, `IOError` |
| **3** | [CodeOrbit_NumberGuessingGame](./CodeOrbit_NumberGuessingGame/) | `random.randint()`, Difficulty levels, Multi-round loop | In-memory session stats | `ValueError`, Bounds checking |
| **4** | [CodeOrbit_FileHandlingRecords](./CodeOrbit_FileHandlingRecords/) | `csv.DictReader`, `csv.DictWriter`, Search, Regex | `records.csv` | `FileNotFoundError`, `PermissionError`, `csv.Error` |
| **5** | [CodeOrbit_DataStructuresPractice](./CodeOrbit_DataStructuresPractice/) | Lists, Sets, Dictionaries, $O(1)$ Hash lookups, Jaccard Index | N/A | Type checks, Missing keys |
| **6** | [CodeOrbit_FileAutomation](./CodeOrbit_FileAutomation/) | `os`, `shutil`, File categorizer, Batch renamer, Dry-run | `automation_log.txt` | `PermissionError`, Collision resolution |

---

## 💻 How to Run Any Project on Windows

### Prerequisites
- Python 3.8+ installed (tested and verified on Python 3.11).
- No external packages (`pip install`) are required — everything is crafted using Python's high-performance Standard Library.

### Quick Run Instructions
Open PowerShell, Command Prompt, or VS Code terminal in the workspace and run:

```powershell
# 1. Simple Calculator
python CodeOrbit_SimpleCalculator/main.py

# 2. To-Do List CLI App
python CodeOrbit_TodoListCLI/main.py

# 3. Number Guessing Game
python CodeOrbit_NumberGuessingGame/main.py

# 4. Student Records Manager
python CodeOrbit_FileHandlingRecords/main.py

# 5. Data Structures Practice
python CodeOrbit_DataStructuresPractice/main.py

# 6. File Automation Script
python CodeOrbit_FileAutomation/main.py
```

---

## 📋 Code Quality & Best Practices
- **PEP 8 Compliance**: Clean naming conventions (`snake_case` functions/variables, `UPPER_CASE` constants).
- **Graceful Error Recovery**: No abrupt program crashes when given malformed input.
- **Zero Third-Party Dependencies**: Self-contained and runs immediately out of the box on any machine.
- **Beginner-Friendly Clarity**: Explicit type annotations and informative docstrings throughout.

---

## 🎓 Internship Deliverables
For step-by-step guidance on uploading to GitHub, posting on LinkedIn, recording the explanation video, and acing the review interview, refer to [SUBMISSION_GUIDE.md](./SUBMISSION_GUIDE.md).

---
**Organization**: CodeOrbit Tech (https://codeorbittech.in)  
**Location**: Bangalore, India  
**Program**: Python Programming Internship (2-Month Duration Tier)
