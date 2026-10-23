# CodeOrbit_TodoListCLI

An interactive, beginner-friendly Command Line Interface (CLI) To-Do List Application built in Python for the **CodeOrbit Tech Python Programming Internship**.

---

## 📌 Project Overview
The **To-Do List CLI App** manages daily tasks directly through the console. It stores tasks in Python data structures during runtime and synchronizes them to a persistent text file (`tasks.txt`), ensuring tasks persist across sessions.

---

## 🚀 Features
- **Task Management**:
  - View tasks in a formatted, numbered table with completion indicators.
  - Add new tasks with input validation.
  - Mark tasks as completed (`[✓]`).
  - Delete/remove tasks by list index.
- **Data Persistence**:
  - Automatically loads existing tasks from `tasks.txt` on launch.
  - Automatically saves on additions, completions, removals, and application exit.
- **Robust Exception Handling**:
  - Out-of-range index detection.
  - Non-numeric input checks.
  - Graceful file I/O recovery if `tasks.txt` is missing.

---

## 🛠️ Requirements & Tech Stack
- **Language**: Python 3.8+ (tested on Python 3.11)
- **Dependencies**: Python Standard Library only (`os`, `sys`).

---

## 💻 How to Run on Windows

### Option 1: Using VS Code
1. Open VS Code.
2. Open the folder: `CodeOrbit_TodoListCLI`.
3. Open `main.py` and run it via `Ctrl + F5` or the Play button.

### Option 2: Using Terminal / PowerShell
1. Open PowerShell or Command Prompt.
2. Navigate to the project directory:
   ```powershell
   cd "d:\Badges\CodeOrbit Task\CodeOrbit_TodoListCLI"
   ```
3. Run:
   ```powershell
   python main.py
   ```

---

## 🧪 Test Cases & Sample Output

### Viewing and Adding Tasks
```text
Welcome to CodeOrbit To-Do List CLI App!
Loaded 4 task(s) from tasks.txt.

--- To-Do List Menu ---
1. View Tasks
2. Add Task
3. Mark Task as Completed
4. Remove Task
5. Save Tasks to File
6. Exit
Select an option (1-6): 1

================================================
                 MY TO-DO LIST                  
================================================
   1. [ ] Review CodeOrbit Python Tasks PDF [Pending]
   2. [ ] Complete Simple Calculator Task  [Pending]
   3. [ ] Build To-Do List CLI App         [Pending]
   4. [ ] Push completed projects to GitHub [Pending]
================================================
```

### Completing a Task
```text
Select an option (1-6): 3
Enter task number to mark as completed: 2
[Success] Task #2 marked as completed!
```

---

## 📚 Code Architecture
- `load_tasks()`: Reads `tasks.txt` and parses each line into a dictionary with `title` and `done` flags.
- `save_tasks()`: Writes tasks back to `tasks.txt`.
- `display_tasks()`: Prints an aligned numbered list.
- `add_task()` / `mark_task_completed()` / `remove_task()`: Handles CRUD operations with input validation.
- `main()`: Contains the navigation loop.

---

## 👤 Author
Developed for the **CodeOrbit Tech Python Programming Internship**.
