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

## Purpose

This project is intended as a practical way to explore Python fundamentals through experimentation rather than only reading theory.

The examples are intentionally small so they can be read, executed, and modified while learning.

## License

This project is licensed under the MIT License. See the LICENSE file for details.