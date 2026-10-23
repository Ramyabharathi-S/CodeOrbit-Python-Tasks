# CodeOrbit_NumberGuessingGame

An engaging, replayable CLI Number Guessing Game developed in Python for the **CodeOrbit Tech Python Programming Internship**.

---

## 📌 Project Overview
The **Number Guessing Game** challenges players to find a randomly generated secret integer within a designated range. The program gives intelligent proximity hints (`Too high` / `Too low`), tallies attempts, evaluates user performance, and maintains session statistics across multiple rounds.

---

## 🚀 Features
- **Dynamic Random Generation**: Uses Python's `random.randint()` for unbiased secret number selection.
- **Adjustable Difficulty**:
  - Easy: 1 to 50
  - Medium: 1 to 100 (Default)
  - Hard: 1 to 200
- **Smart Feedback**:
  - Direct "Too HIGH" / "Too LOW" hints.
  - Proximity hint ("Getting warm!") when within 5 units.
- **Robust Input Validation**:
  - Catches invalid non-integer characters (`ValueError`).
  - Flags out-of-range guesses without penalizing attempt count.
- **Multi-Round Game Loop & Statistics**:
  - Allows playing continuous rounds without restarting the program.
  - Generates an end-of-game summary with total rounds, best score, and average attempts.

---

## 🛠️ Requirements & Tech Stack
- **Language**: Python 3.8+ (tested on Python 3.11)
- **Dependencies**: Python Standard Library only (`random`, `sys`).

---

## 💻 How to Run on Windows

### Option 1: Using VS Code
1. Open VS Code.
2. Open the folder: `CodeOrbit_NumberGuessingGame`.
3. Open `main.py` and run it via `Ctrl + F5` or the Play icon.

### Option 2: Using Windows Terminal / PowerShell
1. Open PowerShell or Command Prompt.
2. Navigate to the project directory:
   ```powershell
   cd "d:\Badges\CodeOrbit Task\CodeOrbit_NumberGuessingGame"
   ```
3. Run:
   ```powershell
   python main.py
   ```

---

## 🧪 Test Cases & Sample Output

```text
====================================================
      CODEORBIT TECH - NUMBER GUESSING GAME         
====================================================
Welcome! Test your intuition and deduction skills.

Select Difficulty Level:
  1. Easy   (Range: 1 to 50)
  2. Medium (Range: 1 to 100) [Default]
  3. Hard   (Range: 1 to 200)
Enter difficulty (1/2/3, press Enter for Medium): 1

==================================================
               ROUND 1 (Easy)               
==================================================
I have selected a secret number between 1 and 50.
Can you guess what it is? Enter your guesses below.
--------------------------------------------------
Attempt #1 - Enter your guess: 25
-> Too LOW! Try a higher number.
Attempt #2 - Enter your guess: 37
-> Too HIGH! Try a lower number. (Getting warm!)
Attempt #3 - Enter your guess: 32
-> Too HIGH! Try a lower number. (Getting warm!)
Attempt #4 - Enter your guess: 30

**************************************************
 BINGO! You guessed the secret number: 30!
 Total attempts taken in this round: 4
**************************************************
Performance: Legendary! Mind reader level!

Would you like to play another round? (y/n): n

====================================================
                 GAME OVER - SUMMARY                
====================================================
Total rounds played : 1
Best score (fewest) : 4 attempts
Average attempts    : 4.0 per round
====================================================
```

---

## 📚 Code Architecture
- `get_difficulty_range()`: Prompts and validates chosen range.
- `play_single_round()`: Contains the core game loop, guess validation, attempt incrementing, and feedback.
- `main()`: Manages session statistics and the replay loop.

---

## 👤 Author
Developed for the **CodeOrbit Tech Python Programming Internship**.
