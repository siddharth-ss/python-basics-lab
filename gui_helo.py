"""GUI wrapper for the Python Basics Lab — runs lessons in a popup window."""

import sys
import io
import contextlib
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

from lessons import LESSONS, run_lesson


class LessonGUI:
    """A simple Tkinter GUI to display lessons in a popup window."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Python Basics Lab")
        self.root.geometry("700x550")
        self.root.minsize(600, 450)

        # Configure style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Title.TLabel", font=("Segoe UI", 14, "bold"))
        style.configure("Lesson.TLabel", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 11, "bold"))

        self.root.option_add("*Font", "Segoe UI 10")

        self._build_ui()

    def _build_ui(self) -> None:
        # Main container
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="🐍 Python Basics Lab",
            style="Title.TLabel",
            foreground="#2E86C1"
        )
        title_label.pack(pady=(0, 5))

        subtitle = ttk.Label(
            main_frame,
            text="Learn Python one small example at a time",
            foreground="#7F8C8D"
        )
        subtitle.pack(pady=(0, 15))

        # Lesson list frame
        list_frame = ttk.LabelFrame(main_frame, text="Lessons", padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # Treeview for lessons
        columns = ("#", "Title")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=12)
        self.tree.heading("#", text="#")
        self.tree.heading("Title", text="Lesson")
        self.tree.column("#", width=40, anchor=tk.CENTER)
        self.tree.column("Title", width=500)

        # Populate lessons
        for i, lesson in enumerate(LESSONS, 1):
            self.tree.insert("", tk.END, values=(i, lesson.title), tags=(f"lesson{i}",))

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for tree
        tree_scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=tree_scroll.set)

        # Bind double-click and Enter key
        self.tree.bind("<Double-1>", self._on_lesson_select)
        self.tree.bind("<Return>", self._on_lesson_select)

        # Buttons frame
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=(5, 0))

        run_btn = ttk.Button(btn_frame, text="▶ Run Selected Lesson", command=self._run_selected)
        run_btn.pack(side=tk.LEFT, padx=(0, 10))

        quit_btn = ttk.Button(btn_frame, text="✕ Exit", command=self.root.quit)
        quit_btn.pack(side=tk.RIGHT)

        # Status bar
        self.status_var = tk.StringVar(value="Select a lesson and click Run")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, foreground="#7F8C8D")
        status_label.pack(anchor=tk.W, pady=(10, 0))

    def _on_lesson_select(self, event=None) -> None:
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            lesson_num = item["values"][0]
            self.status_var.set(f"Selected: Lesson {lesson_num} — {item['values'][1]}")

    def _run_selected(self) -> None:
        selection = self.tree.selection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select a lesson first.")
            return

        item = self.tree.item(selection[0])
        lesson_num = item["values"][0]
        lesson = LESSONS[lesson_num - 1]

        # Open popup with lesson output
        self._show_lesson_popup(lesson)

    def _show_lesson_popup(self, lesson) -> None:
        """Display lesson output in a modal popup window."""
        popup = tk.Toplevel(self.root)
        popup.title(f"Lesson: {lesson.title}")
        popup.geometry("650x500")
        popup.minsize(500, 350)
        popup.transient(self.root)
        popup.grab_set()  # Make it modal

        # Center on parent
        popup.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - (popup.winfo_width() // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (popup.winfo_height() // 2)
        popup.geometry(f"+{x}+{y}")

        # Main frame
        frame = ttk.Frame(popup, padding=15)
        frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(
            frame,
            text=lesson.title,
            style="Header.TLabel",
            foreground="#2E86C1"
        )
        title_label.pack(anchor=tk.W, pady=(0, 5))

        # Explanation
        expl_frame = ttk.LabelFrame(frame, text="Explanation", padding=10)
        expl_frame.pack(fill=tk.X, pady=(0, 10))

        expl_text = tk.Text(expl_frame, height=3, wrap=tk.WORD, relief=tk.FLAT, background="#F8F9FA")
        expl_text.insert(tk.END, lesson.explanation)
        expl_text.configure(state=tk.DISABLED)
        expl_text.pack(fill=tk.X)

        # Output area
        output_frame = ttk.LabelFrame(frame, text="Example Output", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True)

        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            wrap=tk.WORD,
            font=("Consolas", 10),
            background="#1E1E1E",
            foreground="#D4D4D4",
            insertbackground="white",
            relief=tk.FLAT
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # Capture and run the lesson
        self._capture_and_display(lesson)

        # Close button
        close_btn = ttk.Button(frame, text="Close", command=popup.destroy)
        close_btn.pack(pady=(10, 0))

    def _capture_and_display(self, lesson) -> None:
        """Run the lesson example and capture stdout to display in the text widget."""
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = captured_output = io.StringIO()

        try:
            # Run the lesson example (this prints to stdout)
            lesson.example()
            output = captured_output.getvalue()
        finally:
            sys.stdout = old_stdout

        # Display in the text widget
        self.output_text.insert(tk.END, output)
        self.output_text.configure(state=tk.DISABLED)
        self.output_text.see(tk.END)


def main():
    root = tk.Tk()
    app = LessonGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()