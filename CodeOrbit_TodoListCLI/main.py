"""
CodeOrbit Tech - Python Programming Internship
Project: To-Do List CLI App
File: main.py
Description: A functional, clean command-line To-Do List application.
             Allows users to add, view, complete, and remove tasks,
             with automatic text-file persistence (tasks.txt).
"""

import os

TASKS_FILE = "tasks.txt"


def load_tasks(filepath: str = TASKS_FILE) -> list:
    """
    Load tasks from a text file into memory as a list of dicts.
    Each task has: {'title': str, 'done': bool}
    """
    tasks = []
    if not os.path.exists(filepath):
        return tasks

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # Format: [x] Task title OR [ ] Task title
                if line.startswith("[x] "):
                    tasks.append({"title": line[4:].strip(), "done": True})
                elif line.startswith("[ ] "):
                    tasks.append({"title": line[4:].strip(), "done": False})
                else:
                    tasks.append({"title": line, "done": False})
    except IOError as err:
        print(f"[Warning] Could not load saved tasks: {err}")

    return tasks


def save_tasks(tasks: list, filepath: str = TASKS_FILE) -> bool:
    """
    Save current runtime list of tasks to a text file.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            for task in tasks:
                status = "[x]" if task.get("done") else "[ ]"
                f.write(f"{status} {task['title']}\n")
        return True
    except IOError as err:
        print(f"[Error] Failed to save tasks to file: {err}")
        return False


def display_tasks(tasks: list):
    """
    Display a formatted, numbered list of all current tasks.
    """
    print("\n" + "=" * 48)
    print("                 MY TO-DO LIST                  ")
    print("=" * 48)

    if not tasks:
        print("  (Your to-do list is currently empty!)")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "DONE" if task["done"] else "Pending"
            symbol = "[X]" if task["done"] else "[ ]"
            print(f"  {idx:2d}. {symbol} {task['title']:<32} [{status}]")

    print("=" * 48)


def add_task(tasks: list):
    """
    Prompt user for a task description and append it to the list.
    """
    title = input("\nEnter task description: ").strip()
    if not title:
        print("[Error] Task description cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"[Success] Task added: \"{title}\"")


def mark_task_completed(tasks: list):
    """
    Mark an existing task as completed by its list number.
    """
    if not tasks:
        print("\n[Notice] No tasks available to mark as completed.")
        return

    display_tasks(tasks)
    choice = input("\nEnter task number to mark as completed: ").strip()
    try:
        idx = int(choice)
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["done"] = True
            save_tasks(tasks)
            print(f"[Success] Task #{idx} marked as completed!")
        else:
            print(f"[Error] Number out of range. Enter 1 to {len(tasks)}.")
    except ValueError:
        print("[Error] Please enter a valid task number.")


def remove_task(tasks: list):
    """
    Remove a task by its numbered index.
    """
    if not tasks:
        print("\n[Notice] No tasks available to remove.")
        return

    display_tasks(tasks)
    choice = input("\nEnter task number to remove: ").strip()
    try:
        idx = int(choice)
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            save_tasks(tasks)
            print(f"[Success] Removed task: \"{removed['title']}\"")
        else:
            print(f"[Error] Number out of range. Enter 1 to {len(tasks)}.")
    except ValueError:
        print("[Error] Please enter a valid task number.")


def print_menu():
    """Display the application navigation menu."""
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Save Tasks to File")
    print("6. Exit")


def main():
    """Main application loop."""
    print("Welcome to CodeOrbit To-Do List CLI App!")
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} task(s) from {TASKS_FILE}.")

    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            if save_tasks(tasks):
                print(f"[Success] Successfully saved {len(tasks)} task(s) to {TASKS_FILE}.")
        elif choice in ("6", "exit", "quit"):
            save_tasks(tasks)
            print(f"\nAll tasks saved to {TASKS_FILE}. Thank you for using CodeOrbit To-Do List!")
            break
        else:
            print("[Error] Invalid option. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
