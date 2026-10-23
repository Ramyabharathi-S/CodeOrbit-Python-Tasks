# CodeOrbit_FileAutomation

A production-ready, practical File Organizer and Bulk Batch Renamer automation script built in Python for the **CodeOrbit Tech Python Programming Internship**.

---

## 📌 Project Overview
Manual file organization of messy directories (e.g. `Downloads`, `Desktop`, project output folders) is repetitive and time-consuming. This script completely automates file classification and batch renaming by detecting file extensions, sorting them into dedicated category subfolders, maintaining execution audit trails, and offering a risk-free **Dry Run Simulation** mode.

---

## 🚀 Features
- **Intelligent Category Sorting**:
  - `Documents`: `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.csv`
  - `Images`: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`
  - `Audio`: `.mp3`, `.wav`, `.aac`, `.flac`
  - `Video`: `.mp4`, `.mkv`, `.mov`, `.avi`
  - `Archives`: `.zip`, `.rar`, `.tar`, `.gz`, `.7z`
  - `Code_and_Scripts`: `.py`, `.js`, `.html`, `.css`, `.json`, `.sql`
  - `Others`: Any miscellaneous unrecognized formats.
- **Dry-Run Preview Mode**:
  - Allows previewing all planned file movements without touching files on disk.
- **Bulk Batch Renamer**:
  - Add uniform prefixes, suffixes, or versioning stamps across folders.
- **Collision Prevention**:
  - Automatically appends timestamp suffixes (`file_143015.txt`) if a target folder already contains a file with the same name, preventing data loss.
- **Sandbox Test Environment Generator**:
  - Built-in option to generate realistic dummy files in `test_files/` to test without affecting personal files.
- **Audit Logging**:
  - Records every file action with timestamps to `automation_log.txt`.

---

## 🛠️ Requirements & Tech Stack
- **Language**: Python 3.8+ (tested on Python 3.11)
- **Dependencies**: Python Standard Library only (`os`, `shutil`, `datetime`, `sys`).

---

## 💻 How to Run on Windows

### Option 1: Using VS Code
1. Open VS Code.
2. Open the folder: `CodeOrbit_FileAutomation`.
3. Open `main.py` and run using `Ctrl + F5`.

### Option 2: Using Terminal / PowerShell
1. Open PowerShell or Command Prompt.
2. Navigate to the project directory:
   ```powershell
   cd "d:\Badges\CodeOrbit Task\CodeOrbit_FileAutomation"
   ```
3. Run:
   ```powershell
   python main.py
   ```

---

## 🧪 Test Cases & Sample Output

### Step 1: Generate Test Sandbox Files
```text
Select an option (1-6): 1
Enter directory name for samples (press Enter for 'test_files'): 
[Success] Created 11 sample test files inside 'test_files/'.
```

### Step 2: Safe Dry-Run Simulation Preview
```text
Select an option (1-6): 2
Enter directory to preview (press Enter for 'test_files'): 

=================================================================
  FILE ORGANIZER: DRY-RUN SIMULATION (No files will be modified)  
=================================================================
  [2026-10-23 21:45:00] Starting organization for directory: test_files (dry_run=True)
  [Plan] Move 'annual_report.pdf' -> 'Documents/annual_report.pdf'
  [Plan] Move 'company_expenses.csv' -> 'Documents/company_expenses.csv'
  [Plan] Move 'data_analysis.py' -> 'Code_and_Scripts/data_analysis.py'
  [Plan] Move 'demo_recording.mp4' -> 'Video/demo_recording.mp4'
  [Plan] Move 'index.html' -> 'Code_and_Scripts/index.html'
  [Plan] Move 'internship_notes.txt' -> 'Documents/internship_notes.txt'
  [Plan] Move 'miscellaneous.xyz' -> 'Others/miscellaneous.xyz'
  [Plan] Move 'podcast_episode.mp3' -> 'Audio/podcast_episode.mp3'
  [Plan] Move 'profile_picture.png' -> 'Images/profile_picture.png'
  [Plan] Move 'project_backup.zip' -> 'Archives/project_backup.zip'
  [Plan] Move 'vacation_photo.jpg' -> 'Images/vacation_photo.jpg'
=================================================================
[Finished] Simulated organization of 11 file(s).
```

### Step 3: Live Execution
```text
Select an option (1-6): 3
Enter directory to organize (press Enter for 'test_files'): 

=================================================================
  FILE ORGANIZER: LIVE EXECUTION  
=================================================================
  [2026-10-23 21:45:10] Moved 'annual_report.pdf' -> 'Documents/annual_report.pdf'
  [2026-10-23 21:45:10] Moved 'company_expenses.csv' -> 'Documents/company_expenses.csv'
  ...
=================================================================
[Finished] Successfully organized 11 file(s).
Audit log saved to: automation_log.txt
```

---

## 📚 Code Architecture
- `get_category_for_extension()`: Dictionary extension matcher.
- `organize_directory()`: Iterates files, creates subfolders dynamically, and moves items using `shutil.move()`.
- `bulk_rename_files()`: Applies pattern transformations with `os.rename()`.
- `log_action()`: Writes audit entries.
- `generate_sample_test_files()`: Test fixture generator.

---

## 👤 Author
Developed for the **CodeOrbit Tech Python Programming Internship**.
