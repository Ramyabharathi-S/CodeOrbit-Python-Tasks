"""
CodeOrbit Tech - Python Programming Internship
Project: Number Guessing Game
File: main.py
Description: An interactive number guessing game with random target generation,
             dynamic hints (too high / too low), attempt tracking,
             customizable difficulty, and multi-round replay loop.
"""

import random


def get_difficulty_range():
    """
    Prompt user to select a difficulty level and return (min_val, max_val, max_attempts).
    """
    print("\nSelect Difficulty Level:")
    print("  1. Easy   (Range: 1 to 50)")
    print("  2. Medium (Range: 1 to 100) [Default]")
    print("  3. Hard   (Range: 1 to 200)")

    choice = input("Enter difficulty (1/2/3, press Enter for Medium): ").strip()
    if choice == "1":
        return 1, 50, "Easy"
    elif choice == "3":
        return 1, 200, "Hard"
    else:
        return 1, 100, "Medium"


def play_single_round(round_number: int) -> int:
    """
    Play one round of the number guessing game.
    Returns the number of attempts taken by the user.
    """
    min_val, max_val, difficulty_name = get_difficulty_range()
    secret_number = random.randint(min_val, max_val)
    attempts = 0

    print("\n" + "=" * 50)
    print(f"               ROUND {round_number} ({difficulty_name})               ")
    print("=" * 50)
    print(f"I have selected a secret number between {min_val} and {max_val}.")
    print("Can you guess what it is? Enter your guesses below.")
    print("-" * 50)

    while True:
        user_input = input(f"Attempt #{attempts + 1} - Enter your guess: ").strip()

        # Input validation
        try:
            guess = int(user_input)
        except ValueError:
            print("[Invalid Input] Please enter a whole integer number.")
            continue

        if guess < min_val or guess > max_val:
            print(f"[Out of Bounds] Your guess must be between {min_val} and {max_val}.")
            continue

        attempts += 1

        if guess < secret_number:
            diff = secret_number - guess
            proximity = " (Getting warm!)" if diff <= 5 else ""
            print(f"-> Too LOW! Try a higher number.{proximity}")
        elif guess > secret_number:
            diff = guess - secret_number
            proximity = " (Getting warm!)" if diff <= 5 else ""
            print(f"-> Too HIGH! Try a lower number.{proximity}")
        else:
            print("\n" + "*" * 50)
            print(f" BINGO! You guessed the secret number: {secret_number}!")
            print(f" Total attempts taken in this round: {attempts}")
            print("*" * 50)

            # Rating
            if attempts <= 4:
                print("Performance: Legendary! Mind reader level!")
            elif attempts <= 7:
                print("Performance: Excellent guessing strategy!")
            elif attempts <= 10:
                print("Performance: Good job! Keep practicing.")
            else:
                print("Performance: You got it! Try binary search next time for fewer guesses.")

            return attempts


def main():
    """Main game controller with multi-round replay loop."""
    print("=" * 52)
    print("      CODEORBIT TECH - NUMBER GUESSING GAME         ")
    print("=" * 52)
    print("Welcome! Test your intuition and deduction skills.")

    round_count = 0
    round_scores = []

    while True:
        round_count += 1
        attempts = play_single_round(round_count)
        round_scores.append(attempts)

        again = input("\nWould you like to play another round? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break

    # Session Summary
    print("\n" + "=" * 52)
    print("                 GAME OVER - SUMMARY                ")
    print("=" * 52)
    print(f"Total rounds played : {round_count}")
    print(f"Best score (fewest) : {min(round_scores)} attempts")
    avg_score = sum(round_scores) / len(round_scores)
    print(f"Average attempts    : {avg_score:.1f} per round")
    print("=" * 52)
    print("Thank you for playing CodeOrbit Number Guessing Game!\n")


if __name__ == "__main__":
    main()
