"""A small interactive project for learning core Python concepts."""

import os

from lessons import LESSONS, run_lesson


RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
DIM = "\033[2m"


def clear_screen() -> None:
    """Clear the terminal window before displaying a new screen."""
    os.system("cls" if os.name == "nt" else "clear")


def line(character: str = "=") -> None:
    print(f"{CYAN}{character * 62}{RESET}")


def show_header() -> None:
    line()
    print(f"{BOLD}{CYAN}                 PYTHON BASICS LAB{RESET}")
    print(f"{DIM}          Learn Python one small example at a time{RESET}")
    line()


def show_menu() -> None:
    show_header()
    print(f"\n{BOLD}Choose a lesson{RESET}\n")
    for number, lesson in enumerate(LESSONS, start=1):
        print(f"  {GREEN}{number:>2}{RESET}  {lesson.title}")
    print(f"\n  {YELLOW} 0{RESET}  Exit")
    line("-")


def main() -> None:
    """Display the lesson menu and run the chosen example."""
    while True:
        clear_screen()
        show_menu()
        choice = input(f"{BOLD}Enter a lesson number: {RESET}").strip()
        if choice == "0":
            clear_screen()
            show_header()
            print(f"\n{GREEN}Happy coding! Keep experimenting.{RESET}\n")
            return

        if not choice.isdigit() or not 1 <= int(choice) <= len(LESSONS):
            print(f"\n{YELLOW}Please enter a number from 0 to {len(LESSONS)}.{RESET}")
            input("Press Enter to try again...")
            continue

        clear_screen()
        show_header()
        run_lesson(LESSONS[int(choice) - 1])
        print()
        line("-")
        input(f"{DIM}Press Enter to return to the menu...{RESET}")


if __name__ == "__main__":
    main()
