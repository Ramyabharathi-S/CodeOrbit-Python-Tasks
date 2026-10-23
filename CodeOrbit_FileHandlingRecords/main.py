"""
CodeOrbit Tech - Python Programming Internship
Project: File Handling Mini Project (Student Records Manager)
File: main.py
Description: A complete CSV file handling application for student records.
             Supports viewing, adding, searching, updating, and deleting records
             with comprehensive exception handling (FileNotFoundError, PermissionError).
"""

import csv
import os
import re

CSV_FILENAME = "records.csv"
FIELDNAMES = ["StudentID", "FullName", "Email", "Course", "Grade"]


def initialize_file_if_missing(filepath: str = CSV_FILENAME):
    """
    Ensure the CSV file exists. If missing, create it and seed with initial sample records.
    """
    if not os.path.exists(filepath):
        try:
            with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
                writer.writeheader()
                sample_data = [
                    {
                        "StudentID": "STU101",
                        "FullName": "Aarav Sharma",
                        "Email": "aarav.sharma@example.com",
                        "Course": "Python Programming",
                        "Grade": "A",
                    },
                    {
                        "StudentID": "STU102",
                        "FullName": "Diya Patel",
                        "Email": "diya.patel@example.com",
                        "Course": "Data Science",
                        "Grade": "A+",
                    },
                    {
                        "StudentID": "STU103",
                        "FullName": "Rohan Verma",
                        "Email": "rohan.v@example.com",
                        "Course": "Web Development",
                        "Grade": "B",
                    },
                ]
                writer.writerows(sample_data)
        except PermissionError:
            print(f"[Error] Permission denied when attempting to create {filepath}.")
        except IOError as err:
            print(f"[Error] File creation error: {err}")


def load_all_records(filepath: str = CSV_FILENAME) -> list:
    """
    Read all records from CSV and return them as a list of dictionaries.
    Handles FileNotFoundError and other I/O exceptions.
    """
    if not os.path.exists(filepath):
        initialize_file_if_missing(filepath)

    records = []
    try:
        with open(filepath, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append(row)
    except FileNotFoundError:
        print(f"[Error] Data file '{filepath}' was not found.")
    except PermissionError:
        print(f"[Error] Cannot open '{filepath}'. File may be open in Excel or another program.")
    except csv.Error as c_err:
        print(f"[Error] CSV parse error: {c_err}")
    except Exception as exc:
        print(f"[Unexpected Error] {exc}")

    return records


def save_all_records(records: list, filepath: str = CSV_FILENAME) -> bool:
    """
    Overwrite the CSV file with the given list of records.
    """
    try:
        with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(records)
        return True
    except PermissionError:
        print(f"[Error] Cannot save to '{filepath}'. Permission denied or file locked.")
        return False
    except IOError as err:
        print(f"[Error] Failed to write data: {err}")
        return False


def display_table(records: list):
    """
    Render records in an ASCII table.
    """
    if not records:
        print("\n  [Notice] No records found.")
        return

    print("\n" + "=" * 80)
    print(f"{'ID':<8} | {'Full Name':<22} | {'Email':<28} | {'Course':<14} | {'Grade':<5}")
    print("-" * 80)
    for r in records:
        print(f"{r.get('StudentID', ''):<8} | {r.get('FullName', ''):<22} | {r.get('Email', ''):<28} | {r.get('Course', ''):<14} | {r.get('Grade', ''):<5}")
    print("=" * 80)
    print(f"Total Records: {len(records)}\n")


def view_records():
    """Operation: Display all student records."""
    records = load_all_records()
    print("\n--- ALL STUDENT RECORDS ---")
    display_table(records)


def add_record():
    """Operation: Add a new student record with validation."""
    records = load_all_records()
    existing_ids = {r["StudentID"].strip().upper() for r in records}

    print("\n--- ADD NEW STUDENT RECORD ---")
    
    # Student ID Validation
    while True:
        stu_id = input("Enter Student ID (e.g. STU104): ").strip().upper()
        if not stu_id:
            print("[Error] Student ID cannot be blank.")
            continue
        if stu_id in existing_ids:
            print(f"[Error] Student ID '{stu_id}' already exists. IDs must be unique.")
            return
        break

    # Full Name Validation
    while True:
        name = input("Enter Full Name: ").strip()
        if not name:
            print("[Error] Name cannot be blank.")
            continue
        break

    # Email Validation
    while True:
        email = input("Enter Email Address: ").strip().lower()
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            print("[Error] Invalid email format (example: name@domain.com).")
            continue
        break

    # Course
    course = input("Enter Course: ").strip() or "General Studies"

    # Grade
    grade = input("Enter Grade (A+, A, B, C, D, F): ").strip().upper() or "N/A"

    new_record = {
        "StudentID": stu_id,
        "FullName": name,
        "Email": email,
        "Course": course,
        "Grade": grade,
    }

    records.append(new_record)
    if save_all_records(records):
        print(f"[Success] Student record for '{name}' (ID: {stu_id}) added successfully!")


def search_records():
    """Operation: Search records by keyword across ID, Name, or Course."""
    records = load_all_records()
    if not records:
        print("\n[Notice] Database is empty. Nothing to search.")
        return

    print("\n--- SEARCH STUDENT RECORDS ---")
    query = input("Enter search term (Student ID, Name, or Course): ").strip().lower()
    if not query:
        print("[Error] Search query cannot be empty.")
        return

    matches = [
        r for r in records
        if query in r.get("StudentID", "").lower()
        or query in r.get("FullName", "").lower()
        or query in r.get("Course", "").lower()
    ]

    print(f"\nSearch results for '{query}':")
    display_table(matches)


def delete_record():
    """Operation: Delete a student record by ID."""
    records = load_all_records()
    if not records:
        print("\n[Notice] No records available to delete.")
        return

    stu_id = input("\nEnter Student ID to delete: ").strip().upper()
    found = next((r for r in records if r["StudentID"].upper() == stu_id), None)

    if not found:
        print(f"[Error] Student with ID '{stu_id}' not found.")
        return

    confirm = input(f"Are you sure you want to delete {found['FullName']} ({stu_id})? (y/n): ").strip().lower()
    if confirm in ("y", "yes"):
        updated_records = [r for r in records if r["StudentID"].upper() != stu_id]
        if save_all_records(updated_records):
            print(f"[Success] Record for '{found['FullName']}' deleted successfully.")
    else:
        print("[Notice] Deletion cancelled.")


def print_menu():
    """Display main menu options."""
    print("\n" + "=" * 45)
    print("  CODEORBIT TECH - STUDENT RECORDS MANAGER   ")
    print("=" * 45)
    print("1. View All Records")
    print("2. Add New Record")
    print("3. Search Records")
    print("4. Delete Record")
    print("5. Exit")
    print("=" * 45)


def main():
    """Main application loop."""
    initialize_file_if_missing()
    print("Welcome to CodeOrbit Student Records Management System!")

    while True:
        print_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            view_records()
        elif choice == "2":
            add_record()
        elif choice == "3":
            search_records()
        elif choice == "4":
            delete_record()
        elif choice in ("5", "exit", "quit"):
            print("\nThank you for using CodeOrbit Records Manager. Goodbye!\n")
            break
        else:
            print("[Error] Invalid option. Please select 1 through 5.")


if __name__ == "__main__":
    main()
