# Python Basics Lab

An interactive Python learning project designed to teach core Python concepts through small, runnable examples.

The project provides both a **command-line interface** and a **Tkinter graphical interface**, allowing each lesson to be explored interactively.

## Features

- 12 interactive Python lessons
- Command-line learning interface
- Tkinter GUI
- Runnable examples for each concept
- Built-in practice challenge
- Basic automated tests
- Small, readable Python source code

## Lessons

The lab covers:

1. Variables and data types
2. Strings
3. Lists and dictionaries
4. Tuples and sets
5. Functions and conditions
6. Loops
7. List comprehensions
8. Error handling
9. Working with files
10. Classes and objects
11. Modules and imports
12. Practice challenge

## Project Structure

```text
python-basics-lab/
├── helo.py
├── gui_helo.py
├── lessons.py
├── test_lessons.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.11+
- Tkinter for the graphical interface

The command-line version uses Python's standard library, so no external packages are required.

## Run the CLI

From the project directory:

```bash
python helo.py
```

Choose a lesson from the interactive menu and follow the examples.

## Run the GUI

```bash
python gui_helo.py
```

The GUI provides a lesson list where individual lessons can be selected and executed in a separate window.

## Run the Tests

```bash
python -m unittest -v
```

The included tests verify the lesson collection and ensure that each lesson contains the required content and executable example.

## Suggested Learning Workflow

For each lesson, use this short practice loop to build understanding:

1. **Run it once** without changing the example so you can see the expected output.
2. **Predict a result** before running it again—for example, what a changed variable or list item will print.
3. **Change one thing** in the example and rerun the lesson to observe the difference.
4. **Explain the result** in your own words, especially how the output follows from the code.
5. **Try the practice challenge** only after working through the earlier concepts.

Keep experiments small and restore your example when you are ready to move on. For the file-handling lesson, follow the displayed pattern in a test folder if you decide to try writing files yourself.

## Purpose

This project is intended as a practical way to explore Python fundamentals through experimentation rather than only reading theory.

The examples are intentionally small so they can be read, executed, and modified while learning.

## License

This project is licensed under the MIT License. See the LICENSE file for details.