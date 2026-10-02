"""Lesson definitions used by the interactive Python Basics program."""

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Lesson:
    """A short explanation paired with executable example code."""

    title: str
    explanation: str
    example: Callable[[], None]


def variables_and_types() -> None:
    name = "Ada"
    age = 28
    is_learning = True

    print(f"name = {name!r} ({type(name).__name__})")
    print(f"age = {age} ({type(age).__name__})")
    print(f"is_learning = {is_learning} ({type(is_learning).__name__})")


def strings() -> None:
    """Show common string operations."""
    message = "  hello, python learner!  "
    clean_message = message.strip().title()

    print("Original:", repr(message))
    print("Cleaned:", clean_message)
    print("First word:", clean_message.split(",")[0])
    print(f"Characters: {len(clean_message)}")


def collections() -> None:
    languages = ["Python", "JavaScript", "Go"]
    scores = {"Ada": 95, "Lin": 88}

    languages.append("Rust")
    print("List:", languages)
    print("First language:", languages[0])
    print("Dictionary:", scores)
    print("Ada's score:", scores["Ada"])


def tuples_and_sets() -> None:
    """Demonstrate immutable tuples and unique-value sets."""
    point = (4, 7)
    tags = {"python", "beginner", "python", "practice"}

    print("Tuple (x, y):", point)
    print("x coordinate:", point[0])
    print("Set removes duplicate values:", tags)
    print("Does it contain 'python'?", "python" in tags)


def functions_and_conditions() -> None:
    def grade(score: int) -> str:
        if score >= 90:
            return "A"
        if score >= 75:
            return "B"
        return "Keep practising"

    for score in (95, 82, 60):
        print(f"Score {score}: {grade(score)}")


def loops() -> None:
    total = 0
    for number in range(1, 6):
        total += number
        print(f"Added {number}; total is now {total}")


def comprehensions() -> None:
    """Build a collection from another collection in one expression."""
    numbers = [1, 2, 3, 4, 5]
    squares = [number ** 2 for number in numbers]
    even_squares = [number ** 2 for number in numbers if number % 2 == 0]

    print("Numbers:", numbers)
    print("Squares:", squares)
    print("Even squares:", even_squares)


def error_handling() -> None:
    text = "not-a-number"
    try:
        value = int(text)
    except ValueError:
        print(f"Cannot convert {text!r} to an integer.")
    else:
        print(value)
    finally:
        print("This runs whether or not an error occurred.")


def files() -> None:
    """Explain safe file handling without changing the user's files."""
    sample_lines = ["Buy milk\n", "Learn Python\n"]
    print("To write a file, use:")
    print("  with open('notes.txt', 'w', encoding='utf-8') as file:")
    print("      file.write('Hello!\\n')")
    print("\nThe 'with' block closes the file automatically.")
    print("Example text that could be read from a file:", end=" ")
    print("".join(sample_lines).replace("\n", "; ").rstrip("; "))


def classes() -> None:
    """Demonstrate a small class with data and behavior."""
    class Book:
        def __init__(self, title: str, pages: int) -> None:
            self.title = title
            self.pages = pages

        def description(self) -> str:
            return f"{self.title} has {self.pages} pages."

    book = Book("Python Basics", 120)
    print(book.description())
    print("A class is a blueprint; an object is one instance of it.")


def modules() -> None:
    """Show an import from Python's standard library."""
    from math import sqrt

    print("sqrt(81) =", sqrt(81))
    print("Modules let you reuse code from another file or library.")


def practice_challenge() -> None:
    """Provide a small challenge and one possible answer."""
    words = ["python", "is", "fun"]
    sentence = " ".join(word.capitalize() for word in words) + "."
    print("Challenge: Turn", words, "into a title-cased sentence.")
    print("One solution:")
    print("  ' '.join(word.capitalize() for word in words) + '.'")
    print("Result:", sentence)


LESSONS = (
    Lesson(
        "Variables and data types",
        "Variables store values. Python infers the type from the value you assign.",
        variables_and_types,
    ),
    Lesson(
        "Strings",
        "Strings are text values. Methods such as strip(), title(), and split() transform or inspect text.",
        strings,
    ),
    Lesson(
        "Lists and dictionaries",
        "Lists are ordered, mutable collections; dictionaries map keys to values.",
        collections,
    ),
    Lesson(
        "Tuples and sets",
        "Tuples keep ordered values that should not change; sets store unique values.",
        tuples_and_sets,
    ),
    Lesson(
        "Functions and conditions",
        "Functions package reusable logic, while if statements choose between paths.",
        functions_and_conditions,
    ),
    Lesson(
        "Loops",
        "A for loop repeats an action for every value in an iterable such as range().",
        loops,
    ),
    Lesson(
        "List comprehensions",
        "A comprehension creates a new list by applying an expression to each item, optionally with a filter.",
        comprehensions,
    ),
    Lesson(
        "Error handling",
        "try/except lets a program recover cleanly from expected errors.",
        error_handling,
    ),
    Lesson(
        "Working with files",
        "Use open() inside a with block to read or write files safely. This lesson only displays the pattern.",
        files,
    ),
    Lesson(
        "Classes and objects",
        "Classes group related data and behavior. Objects are instances created from a class.",
        classes,
    ),
    Lesson(
        "Modules and imports",
        "Imports make functions and classes from other files or libraries available to your program.",
        modules,
    ),
    Lesson(
        "Practice challenge",
        "Try the challenge before reading the displayed example solution.",
        practice_challenge,
    ),
)


def run_lesson(lesson: Lesson) -> None:
    """Print a lesson heading and execute its demonstration."""
    print(f"\n\033[1m\033[93m> {lesson.title}\033[0m")
    print(f"\033[2m{lesson.explanation}\033[0m")
    print("\n\033[1mExample output\033[0m")
    print("\033[96m" + "-" * 31 + "\033[0m")
    lesson.example()
