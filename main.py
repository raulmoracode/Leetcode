#!/usr/bin/env python3

import os
import re
import subprocess
import sys


def discover_exercises(root: str) -> dict[str, str]:
    exercises = {}
    pattern = re.compile(r"^(\d+)\.\s+(.+)$")
    
    for entry in sorted(os.listdir(root)):
        full_path = os.path.join(root, entry)
        if not os.path.isdir(full_path):
            continue
        if entry.startswith("."):
            continue
        
        match = pattern.match(entry)
        if match:
            num = match.group(1)
            exercises[num] = entry
    
    return exercises

def show_menu(exercises: dict[str, str]):

    print("\nAvailable exercises:\n")
    for num, name in sorted(exercises.items(), key=lambda x: int(x[0])):
        print(f"  {num:>3} - {name}")
    print("\n")
    print("    Q - Quit")

def main():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    exercises = discover_exercises(repo_root)
    
    if not exercises:
        print("No exercises found.")
        return
    
    while True:

        show_menu(exercises)

        choice = input("\nEnter exercise number: ").strip().lower()
        
        if choice in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        
        if choice not in exercises:
            print(f"  ✗ Invalid: '{choice}'. Try again.")
            continue
        
        exercise_dir = exercises[choice]
        input_py = os.path.join(repo_root, exercise_dir, "input.py")
        
        if not os.path.exists(input_py):
            print(f"  ✗ Not found: {input_py}")
            continue
        
        print(f"\nRunning: {exercise_dir}")
        print("\n")
        print("" + "-" * 46)
        print("\n")
        
        result = subprocess.run(
            [sys.executable, input_py],
            cwd=os.path.join(repo_root, exercise_dir)
        )

        print("\n")
        print("" + "-" * 46)
        if result.returncode == 0:
            print("  ✓ Completed\n")
        else:
            print(f"  ✗ Failed (exit code: {result.returncode})\n")


if __name__ == "__main__":
    main()