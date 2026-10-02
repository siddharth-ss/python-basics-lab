"""Basic checks for the Python Basics lesson project."""

import unittest

from lessons import LESSONS


class LessonTests(unittest.TestCase):
    def test_project_has_extended_lessons(self) -> None:
        self.assertEqual(len(LESSONS), 12)

    def test_all_lessons_have_content(self) -> None:
        for lesson in LESSONS:
            self.assertTrue(lesson.title)
            self.assertTrue(lesson.explanation)
            self.assertTrue(callable(lesson.example))


if __name__ == "__main__":
    unittest.main()
