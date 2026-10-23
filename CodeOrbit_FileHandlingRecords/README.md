# CodeOrbit_FileHandlingRecords

A robust, beginner-friendly CSV File Handling Mini Project for Student Records Management, developed for the **CodeOrbit Tech Python Programming Internship**.

---

## 📌 Project Overview
The **Student Records Manager** demonstrates practical file I/O operations in Python using Comma Separated Value (CSV) files. The application allows users to view, add, search, and delete student records while gracefully handling file exceptions like missing files and permission blocks.

---

## 🚀 Features
- **CSV Data Persistence**: Stores records in `records.csv` using Python's built-in `csv.DictReader` and `csv.DictWriter`.
- **View Records**: Aligns all student data into a clear ASCII table.
- **Add New Record**:
  - Enforces unique Student IDs (prevents duplicate key conflicts).
  - Validates email syntax using regex.
  - Automatically writes and flushes updates to disk.
- **Case-Insensitive Search**:
  - Search across Student ID, Full Name, or Course.
- **Delete Record**:
  - Safe record removal with user confirmation.
- **Defensive Error Handling**:
  - Auto-initializes `records.csv` with sample data if the file does not exist (`FileNotFoundError`).
  - Catches `PermissionError` (e.g. if the CSV file is open in Microsoft Excel).
  - Handles parsing and corrupted format errors gracefully.

---

## 🛠️ Requirements & Tech Stack
- **Language**: Python 3.8+ (tested on Python 3.11)
- **Dependencies**: Python Standard Library only (`csv`, `os`, `re`, `sys`).

---

## 💻 How to Run on Windows

### Option 1: Using VS Code
1. Open VS Code.
2. Open the folder: `CodeOrbit_FileHandlingRecords`.
3. Open `main.py` and run with `Ctrl + F5`.

### Option 2: Using Terminal / PowerShell
1. Open PowerShell or Command Prompt.
2. Navigate to the project directory:
   ```powershell
   cd "d:\Badges\CodeOrbit Task\CodeOrbit_FileHandlingRecords"
   ```
3. Run:
   ```powershell
   python main.py
   ```

---

## 🧪 Test Cases & Sample Output

### Viewing Records
```text
================================================================================
ID       | Full Name              | Email                        | Course         | Grade
--------------------------------------------------------------------------------
STU101   | Aarav Sharma           | aarav.sharma@example.com     | Python Programming | A    
STU102   | Diya Patel             | diya.patel@example.com       | Data Science   | A+   
STU103   | Rohan Verma            | rohan.v@example.com          | Web Development| B    
================================================================================
Total Records: 3
```

### Searching Records
```text
Enter search term (Student ID, Name, or Course): python

Search results for 'python':
================================================================================
ID       | Full Name              | Email                        | Course         | Grade
--------------------------------------------------------------------------------
STU101   | Aarav Sharma           | aarav.sharma@example.com     | Python Programming | A    
================================================================================
Total Records: 1
```

---

## 📚 Code Architecture
- `initialize_file_if_missing()`: Generates initial template schema and seed data if CSV is absent.
- `load_all_records()`: Safely reads records with `csv.DictReader` and exception recovery.
- `save_all_records()`: Writes back records with `csv.DictWriter`.
- `display_table()`: Formats records into aligned terminal tables.
- `add_record()` / `search_records()` / `delete_record()`: Business logic.

---

## 👤 Author
Developed for the **CodeOrbit Tech Python Programming Internship**.
