# CodeOrbit_DataStructuresPractice

A structured, beginner-friendly practice suite solving 4 core computational problems using Python Lists, Dictionaries, and Sets, built for the **CodeOrbit Tech Python Programming Internship**.

---

## 📌 Project Overview
This project demonstrates proficiency with Python's primary built-in data structures. It provides clean, modular solutions with time-complexity considerations ($O(1)$ lookups) for:
1. **Duplicate Remover & Set Algebra** (Lists & Sets)
2. **Text Analyzer & Word Frequency Counter** (Dictionaries)
3. **Student Gradebook & Analytics Engine** (Nested Dictionaries & Lists)
4. **Mutual Connections & Interest Matcher** (Mathematical Sets & Jaccard Similarity)

---

## 🚀 Problems Implemented

### Problem 1: Order-Preserving Duplicate Remover & Set Operations
- **Data Structures**: `list`, `set`
- Removes duplicates from collections without disrupting initial sequence order ($O(N)$ runtime).
- Demonstrates mathematical set operations:
  - Union (`A | B`)
  - Intersection (`A & B`)
  - Difference (`A - B`)
  - Symmetric Difference (`A ^ B`)

### Problem 2: Word Frequency Counter & Text Analyzer
- **Data Structures**: `dict`, `str`, `list`
- Strips punctuation and normalizes casing.
- Aggregates word occurrences using dictionary hashing (`dict.get(key, 0) + 1`).
- Sorts and extracts the top $N$ most frequent terms.

### Problem 3: Student Gradebook Analytics Engine
- **Data Structures**: `dict` (nested with `list`)
- Maps student identifiers to arrays of exam scores.
- Computes aggregate metrics: total points, arithmetic mean, highest student, and automated letter grades (A+, A, B, C, F).

### Problem 4: Social Network Mutual Interests Matcher
- **Data Structures**: `set`
- Evaluates shared vs. exclusive hobbies between two profiles.
- Computes the Jaccard similarity index: $\frac{|A \cap B|}{|A \cup B|} \times 100\%$.

---

## 🛠️ Requirements & Tech Stack
- **Language**: Python 3.8+ (tested on Python 3.11)
- **Dependencies**: Python Standard Library only (`string`, `sys`).

---

## 💻 How to Run on Windows

### Option 1: Using VS Code
1. Open VS Code.
2. Open the folder: `CodeOrbit_DataStructuresPractice`.
3. Open `main.py` and run using `Ctrl + F5`.

### Option 2: Using Terminal / PowerShell
1. Open PowerShell or Command Prompt.
2. Navigate to the project directory:
   ```powershell
   cd "d:\Badges\CodeOrbit Task\CodeOrbit_DataStructuresPractice"
   ```
3. Run:
   ```powershell
   python main.py
   ```

---

## 🧪 Test Cases & Sample Output

Select option `1` to run all four problem demonstrations in one automated showcase:

```text
#################################################################
   RUNNING ALL 4 DATA STRUCTURE PRACTICE PROBLEMS (DEMO MODE)    
#################################################################

============================================================
  PROBLEM 1: Duplicate Remover & Set Operations (Lists & Sets)  
============================================================
Original list with duplicates : ['apple', 'banana', 'apple', 'orange', 'banana', 'kiwi', 'apple']
Duplicates removed (ordered)  : ['apple', 'banana', 'orange', 'kiwi']

Set Operations on Tech Skills:
  Team A Skills        : {'Python', 'Java', 'JavaScript', 'C++'}
  Team B Skills        : {'Python', 'Go', 'Rust', 'Java'}
  Combined (Union)     : {'Go', 'Python', 'Rust', 'Java', 'JavaScript', 'C++'}
  Common (Intersection): {'Python', 'Java'}
  Only Team A (Diff)   : {'JavaScript', 'C++'}
  Unique to Either     : {'Go', 'JavaScript', 'C++', 'Rust'}

============================================================
  PROBLEM 2: Word Frequency Counter (Dictionaries)              
============================================================
Input Text:
  "Python is powerful and Python is fun. CodeOrbit helps you learn Python step by step with hands-on practice and practical projects."

Statistics: 19 Total Words | 14 Unique Words
Top 3 Most Frequent Words:
  #1: 'python' (appears 3 times)
  #2: 'is' (appears 2 times)
  #3: 'and' (appears 2 times)
```

---

## 📚 Code Architecture
- Pure functions per task: `remove_duplicates_ordered()`, `perform_set_operations()`, `count_word_frequencies()`, `calculate_student_analytics()`, and `analyze_shared_interests()`.
- Interactive CLI + Automated demonstration harness for presentations and reviews.

---

## 👤 Author
Developed for the **CodeOrbit Tech Python Programming Internship**.
