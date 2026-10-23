"""
CodeOrbit Tech - Python Programming Internship
Project: Mini Project - Simple Automation Script
File: main.py
Description: Automated File Organizer & Bulk Batch Renamer with safe dry-run mode,
             execution audit logging, and automated sample test-data generation.
"""

import datetime
import os
import shutil

# Default category mappings based on file extensions
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv", ".rtf"],
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp", ".webp"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Video": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code_and_Scripts": [".py", ".js", ".html", ".css", ".json", ".sql", ".sh", ".bat"],
}

LOG_FILE = "automation_log.txt"


def log_action(message: str, log_filepath: str = LOG_FILE):
    """Append a timestamped log entry to the log file and print to console."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(f"  {entry}")
    try:
        with open(log_filepath, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except IOError:
        pass


def get_category_for_extension(ext: str) -> str:
    """Determine destination category subfolder for a given file extension."""
    ext = ext.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


def generate_sample_test_files(target_dir: str = "test_files"):
    """
    Generate dummy files inside a sandbox test directory to allow
    safe, instant testing of the automation script.
    """
    os.makedirs(target_dir, exist_ok=True)
    sample_files = [
        "annual_report.pdf",
        "internship_notes.txt",
        "company_expenses.csv",
        "profile_picture.png",
        "vacation_photo.jpg",
        "podcast_episode.mp3",
        "demo_recording.mp4",
        "project_backup.zip",
        "data_analysis.py",
        "index.html",
        "miscellaneous.xyz",
    ]

    for fname in sample_files:
        path = os.path.join(target_dir, fname)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"Sample dummy data for {fname}\nCreated for CodeOrbit Automation Test.\n")

    print(f"\n[Success] Created {len(sample_files)} sample test files inside '{target_dir}/'.")


def organize_directory(directory_path: str, dry_run: bool = False):
    """
    Organize all files in directory_path into category folders.
    If dry_run is True, simulates operations without moving files.
    """
    if not os.path.exists(directory_path):
        print(f"[Error] Target directory '{directory_path}' does not exist.")
        return

    items = os.listdir(directory_path)
    # Filter only files, skip directories and script files
    files_to_move = [
        f for f in items
        if os.path.isfile(os.path.join(directory_path, f))
        and f not in ("main.py", LOG_FILE, "automation_log.txt")
    ]

    if not files_to_move:
        print(f"\n[Notice] No loose files found in '{directory_path}' to organize.")
        return

    mode_label = "DRY-RUN SIMULATION (No files will be modified)" if dry_run else "LIVE EXECUTION"
    print("\n" + "=" * 65)
    print(f"  FILE ORGANIZER: {mode_label}  ")
    print("=" * 65)
    log_action(f"Starting organization for directory: {directory_path} (dry_run={dry_run})")

    moved_count = 0
    for filename in files_to_move:
        src_path = os.path.join(directory_path, filename)
        _, ext = os.path.splitext(filename)
        category = get_category_for_extension(ext)
        dest_folder = os.path.join(directory_path, category)
        dest_path = os.path.join(dest_folder, filename)

        if dry_run:
            print(f"  [Plan] Move '{filename}' -> '{category}/{filename}'")
            moved_count += 1
        else:
            try:
                os.makedirs(dest_folder, exist_ok=True)
                # Avoid collision if destination file already exists
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(filename)
                    timestamp_suffix = datetime.datetime.now().strftime("%H%M%S")
                    new_filename = f"{base}_{timestamp_suffix}{ext}"
                    dest_path = os.path.join(dest_folder, new_filename)

                shutil.move(src_path, dest_path)
                log_action(f"Moved '{filename}' -> '{category}/{os.path.basename(dest_path)}'")
                moved_count += 1
            except PermissionError:
                log_action(f"Permission denied for '{filename}' - skipping.")
            except Exception as err:
                log_action(f"Error moving '{filename}': {err}")

    print("=" * 65)
    action_type = "Simulated organization of" if dry_run else "Successfully organized"
    print(f"[Finished] {action_type} {moved_count} file(s).")
    if not dry_run:
        print(f"Audit log saved to: {LOG_FILE}\n")


def bulk_rename_files(directory_path: str, prefix: str = "", suffix: str = "", dry_run: bool = False):
    """
    Bulk rename all files in a directory by adding a prefix and/or suffix.
    """
    if not os.path.exists(directory_path):
        print(f"[Error] Target directory '{directory_path}' does not exist.")
        return

    items = os.listdir(directory_path)
    files = [
        f for f in items
        if os.path.isfile(os.path.join(directory_path, f))
        and f not in ("main.py", LOG_FILE)
    ]

    if not files:
        print(f"\n[Notice] No files found in '{directory_path}' to rename.")
        return

    mode_label = "DRY-RUN SIMULATION" if dry_run else "LIVE EXECUTION"
    print("\n" + "=" * 65)
    print(f"  BULK BATCH RENAMER: {mode_label}  ")
    print("=" * 65)

    renamed_count = 0
    for idx, filename in enumerate(files, start=1):
        name, ext = os.path.splitext(filename)
        new_filename = f"{prefix}{name}{suffix}{ext}"
        src_path = os.path.join(directory_path, filename)
        dest_path = os.path.join(directory_path, new_filename)

        if dry_run:
            print(f"  [Plan] '{filename}' -> '{new_filename}'")
            renamed_count += 1
        else:
            try:
                os.rename(src_path, dest_path)
                log_action(f"Renamed: '{filename}' -> '{new_filename}'")
                renamed_count += 1
            except Exception as err:
                log_action(f"Failed to rename '{filename}': {err}")

    print("=" * 65)
    print(f"[Finished] Renamed {renamed_count} file(s).\n")


def print_menu():
    print("\n" + "=" * 52)
    print("  CODEORBIT TECH - FILE AUTOMATION UTILITY  ")
    print("=" * 52)
    print("1. Generate Sample Test Files (Sandbox)")
    print("2. Preview Organization (Safe Dry-Run)")
    print("3. Organize Files into Category Folders (Live)")
    print("4. Bulk Batch Rename Files")
    print("5. View Activity Audit Log")
    print("6. Exit")
    print("=" * 52)


def view_audit_log():
    if not os.path.exists(LOG_FILE):
        print("\n[Notice] No audit log file found yet.")
        return
    print("\n--- RECENT ACTIVITY AUDIT LOG ---")
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[-20:]:  # Last 20 lines
                print(line.rstrip())
    except IOError as err:
        print(f"[Error] Could not read log file: {err}")


def main():
    print("Welcome to CodeOrbit Automated File Organizer!")

    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            target = input("Enter directory name for samples (press Enter for 'test_files'): ").strip() or "test_files"
            generate_sample_test_files(target)

        elif choice == "2":
            target = input("Enter directory to preview (press Enter for 'test_files'): ").strip() or "test_files"
            organize_directory(target, dry_run=True)

        elif choice == "3":
            target = input("Enter directory to organize (press Enter for 'test_files'): ").strip() or "test_files"
            organize_directory(target, dry_run=False)

        elif choice == "4":
            target = input("Enter directory containing files to rename: ").strip() or "test_files"
            prefix = input("Enter prefix to add (e.g., 'Doc_'): ").strip()
            suffix = input("Enter suffix to add (e.g., '_v1'): ").strip()
            is_dry = input("Preview only with dry-run? (y/n, default y): ").strip().lower()
            dry_run = is_dry not in ("n", "no")
            bulk_rename_files(target, prefix=prefix, suffix=suffix, dry_run=dry_run)

        elif choice == "5":
            view_audit_log()

        elif choice in ("6", "exit", "quit"):
            print("\nThank you for using CodeOrbit File Automation. Goodbye!\n")
            break

        else:
            print("[Error] Invalid option. Please select 1 through 6.")


if __name__ == "__main__":
    main()
