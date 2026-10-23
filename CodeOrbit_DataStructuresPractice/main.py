"""
CodeOrbit Tech - Python Programming Internship
Project: Simple Data Structures Practice
File: main.py
Description: Practical implementations solving 4 core problems using Python
             Lists, Dictionaries, and Sets with clean functions, comprehensive
             comments, interactive menus, and an automated showcase runner.
"""

import string


# ==============================================================================
# PROBLEM 1: Lists & Sets - Duplicate Remover & Set Operations
# ==============================================================================
def remove_duplicates_ordered(input_list: list) -> list:
    """
    Remove duplicate items from a list while preserving original insertion order.
    Uses a set for O(1) membership lookups.
    """
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list


def perform_set_operations(set_a: set, set_b: set) -> dict:
    """
    Perform core mathematical set operations between two sets:
    Union, Intersection, Difference, and Symmetric Difference.
    """
    return {
        "set_a": set_a,
        "set_b": set_b,
        "union": set_a | set_b,
        "intersection": set_a & set_b,
        "difference_a_minus_b": set_a - set_b,
        "symmetric_difference": set_a ^ set_b,
    }


def run_problem_1():
    """Interactive / Demo runner for Problem 1."""
    print("\n" + "=" * 60)
    print("  PROBLEM 1: Duplicate Remover & Set Operations (Lists & Sets)  ")
    print("=" * 60)
    
    sample_list = ["apple", "banana", "apple", "orange", "banana", "kiwi", "apple"]
    print(f"Original list with duplicates : {sample_list}")
    deduped = remove_duplicates_ordered(sample_list)
    print(f"Duplicates removed (ordered)  : {deduped}")

    list_a = {"Python", "JavaScript", "C++", "Java"}
    list_b = {"Python", "Go", "Rust", "Java"}
    results = perform_set_operations(list_a, list_b)

    print("\nSet Operations on Tech Skills:")
    print(f"  Team A Skills        : {results['set_a']}")
    print(f"  Team B Skills        : {results['set_b']}")
    print(f"  Combined (Union)     : {results['union']}")
    print(f"  Common (Intersection): {results['intersection']}")
    print(f"  Only Team A (Diff)   : {results['difference_a_minus_b']}")
    print(f"  Unique to Either     : {results['symmetric_difference']}")


# ==============================================================================
# PROBLEM 2: Dictionaries - Text Analyzer & Word Frequency Counter
# ==============================================================================
def count_word_frequencies(text: str) -> dict:
    """
    Clean text, strip punctuation, convert to lowercase, and return
    a dictionary of {word: frequency_count}.
    """
    # Remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()

    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict


def get_top_frequent_words(freq_dict: dict, top_n: int = 3) -> list:
    """
    Return top N most frequent words sorted by descending count.
    """
    sorted_items = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_items[:top_n]


def run_problem_2():
    """Interactive / Demo runner for Problem 2."""
    print("\n" + "=" * 60)
    print("  PROBLEM 2: Word Frequency Counter (Dictionaries)              ")
    print("=" * 60)
    sample_text = (
        "Python is powerful and Python is fun. CodeOrbit helps you learn "
        "Python step by step with hands-on practice and practical projects."
    )
    print("Input Text:")
    print(f"  \"{sample_text}\"")

    frequencies = count_word_frequencies(sample_text)
    total_words = sum(frequencies.values())
    unique_words = len(frequencies)

    print(f"\nStatistics: {total_words} Total Words | {unique_words} Unique Words")
    print("All Word Counts (Dictionary):")
    for word, count in sorted(frequencies.items()):
        print(f"  - '{word}': {count}")

    top_words = get_top_frequent_words(frequencies, top_n=3)
    print(f"\nTop 3 Most Frequent Words:")
    for rank, (w, count) in enumerate(top_words, start=1):
        print(f"  #{rank}: '{w}' (appears {count} times)")


# ==============================================================================
# PROBLEM 3: Dictionaries & Lists - Student Gradebook & Statistics Engine
# ==============================================================================
def calculate_student_analytics(gradebook: dict) -> dict:
    """
    Compute total, average score, and letter grade for each student.
    Find overall top student.
    """
    def letter_grade(avg: float) -> str:
        if avg >= 90: return "A+"
        if avg >= 80: return "A"
        if avg >= 70: return "B"
        if avg >= 60: return "C"
        return "F"

    summary = {}
    highest_avg = -1.0
    top_student = None

    for name, scores in gradebook.items():
        total = sum(scores)
        avg = round(total / len(scores), 2) if scores else 0.0
        grade = letter_grade(avg)
        summary[name] = {
            "scores": scores,
            "total": total,
            "average": avg,
            "grade": grade,
        }
        if avg > highest_avg:
            highest_avg = avg
            top_student = name

    return {
        "students": summary,
        "top_student": top_student,
        "highest_avg": highest_avg,
    }


def run_problem_3():
    """Interactive / Demo runner for Problem 3."""
    print("\n" + "=" * 60)
    print("  PROBLEM 3: Student Gradebook & Statistics (Dicts + Lists)     ")
    print("=" * 60)
    
    sample_gradebook = {
        "Aarav": [88, 92, 95, 89],
        "Diya": [94, 98, 91, 96],
        "Rohan": [72, 68, 75, 70],
        "Ananya": [85, 87, 84, 90],
    }

    analytics = calculate_student_analytics(sample_gradebook)

    print(f"{'Student':<12} | {'Scores':<20} | {'Total':<6} | {'Average':<8} | {'Grade':<5}")
    print("-" * 60)
    for name, data in analytics["students"].items():
        scores_str = str(data["scores"])
        print(f"{name:<12} | {scores_str:<20} | {data['total']:<6} | {data['average']:<8.2f} | {data['grade']:<5}")
    print("-" * 60)
    print(f"Top Performer: {analytics['top_student']} with average score of {analytics['highest_avg']}%\n")


# ==============================================================================
# PROBLEM 4: Sets - Mutual Interests & Match Finder
# ==============================================================================
def analyze_shared_interests(person1_name: str, interests1: set, person2_name: str, interests2: set) -> dict:
    """
    Compare interests between two profiles using set algebra.
    Calculates Jaccard similarity index.
    """
    common = interests1 & interests2
    all_interests = interests1 | interests2
    similarity_score = (len(common) / len(all_interests)) * 100 if all_interests else 0.0

    return {
        "common": common,
        "unique_to_1": interests1 - interests2,
        "unique_to_2": interests2 - interests1,
        "similarity_score": round(similarity_score, 1),
    }


def run_problem_4():
    """Interactive / Demo runner for Problem 4."""
    print("\n" + "=" * 60)
    print("  PROBLEM 4: Mutual Connections & Interest Matcher (Sets)       ")
    print("=" * 60)

    p1 = "Dev A"
    interests_a = {"AI", "Python", "Cloud", "Gaming", "Robotics"}
    p2 = "Dev B"
    interests_b = {"Python", "Web Dev", "Robotics", "Design", "AI"}

    analysis = analyze_shared_interests(p1, interests_a, p2, interests_b)

    print(f"Interests of {p1}: {interests_a}")
    print(f"Interests of {p2}: {interests_b}")
    print(f"\nMutual Interests      : {analysis['common']}")
    print(f"Exclusive to {p1}     : {analysis['unique_to_1']}")
    print(f"Exclusive to {p2}     : {analysis['unique_to_2']}")
    print(f"Match Similarity Index: {analysis['similarity_score']}% match")


# ==============================================================================
# MAIN MENU & AUTOMATED DEMO RUNNER
# ==============================================================================
def run_all_demonstrations():
    """Run all 4 problems consecutively with formatted sample data."""
    print("\n" + "#" * 65)
    print("   RUNNING ALL 4 DATA STRUCTURE PRACTICE PROBLEMS (DEMO MODE)    ")
    print("#" * 65)
    run_problem_1()
    run_problem_2()
    run_problem_3()
    run_problem_4()
    print("\n" + "#" * 65)
    print("   ALL 4 DATA STRUCTURE PROBLEMS COMPLETED SUCCESSFULLY!        ")
    print("#" * 65 + "\n")


def print_menu():
    print("\n" + "=" * 50)
    print("  CODEORBIT TECH - DATA STRUCTURES PRACTICE  ")
    print("=" * 50)
    print("1. Run All 4 Problems (Full Automated Showcase)")
    print("2. Problem 1: Duplicate Remover & Set Ops (Lists & Sets)")
    print("3. Problem 2: Word Frequency Counter (Dictionaries)")
    print("4. Problem 3: Student Gradebook Statistics (Dicts + Lists)")
    print("5. Problem 4: Mutual Interests & Set Matcher (Sets)")
    print("6. Exit")
    print("=" * 50)


def main():
    print("Welcome to CodeOrbit Simple Data Structures Practice!")

    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            run_all_demonstrations()
        elif choice == "2":
            run_problem_1()
        elif choice == "3":
            run_problem_2()
        elif choice == "4":
            run_problem_3()
        elif choice == "5":
            run_problem_4()
        elif choice in ("6", "exit", "quit"):
            print("\nThank you for exploring Python Data Structures. Goodbye!\n")
            break
        else:
            print("[Error] Invalid option. Please select 1 through 6.")


if __name__ == "__main__":
    main()
