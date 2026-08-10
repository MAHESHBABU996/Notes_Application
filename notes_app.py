import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import markdown
import tempfile
import webbrowser
import os

DB = "notes.db"


# ---------------- DATABASE ----------------

def create_database():
    con = sqlite3.connect(DB)
    con.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT
        )
    """)
    con.commit()
    con.close()


def get_notes(search=""):
    con = sqlite3.connect(DB)

    if search:
        value = "%" + search + "%"
        notes = con.execute("""
            SELECT id, title, content, tags
            FROM notes
            WHERE title LIKE ?
               OR content LIKE ?
               OR tags LIKE ?
            ORDER BY id DESC
        """, (value, value, value)).fetchall()
    else:
        notes = con.execute("""
            SELECT id, title, content, tags
            FROM notes
            ORDER BY id DESC
        """).fetchall()

    con.close()
    return notes


# ---------------- APPLICATION ----------------

class NotesApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Notes Application")
        self.root.geometry("1000x650")

        self.selected_id = None
        self.notes = []

        self.create_gui()
        self.load_notes()

    # ---------------- GUI ----------------

    def create_gui(self):

        # Search
        search_frame = tk.Frame(self.root)
        search_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(
            search_frame,
            text="Search:"
        ).pack(side="left")

        self.search_box = tk.Entry(
            search_frame,
            width=40
        )
        self.search_box.pack(
            side="left",
            padx=10
        )

        self.search_box.bind(
            "<KeyRelease>",
            self.search_notes
        )

        tk.Button(
            search_frame,
            text="Clear",
            command=self.clear_search
        ).pack(side="left")

        # Main frame
        main = tk.Frame(self.root)
        main.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        # Left side
        left = tk.Frame(main)
        left.pack(
            side="left",
            fill="y",
            padx=(0, 10)
        )

        tk.Label(
            left,
            text="My Notes",
            font=("Arial", 14, "bold")
        ).pack(pady=5)

        self.note_list = tk.Listbox(
            left,
            width=35,
            height=25
        )
        self.note_list.pack(
            fill="y",
            expand=True
        )

        self.note_list.bind(
            "<<ListboxSelect>>",
            self.select_note
        )

        # Right side
        right = tk.Frame(main)
        right.pack(
            side="left",
            fill="both",
            expand=True
        )

        tk.Label(
            right,
            text="Title"
        ).pack(anchor="w")

        self.title_box = tk.Entry(
            right,
            font=("Arial", 14)
        )
        self.title_box.pack(
            fill="x",
            pady=(3, 10)
        )

        tk.Label(
            right,
            text="Tags (comma separated)"
        ).pack(anchor="w")

        self.tags_box = tk.Entry(right)
        self.tags_box.pack(
            fill="x",
            pady=(3, 10)
        )

        tk.Label(
            right,
            text="Content (Markdown)"
        ).pack(anchor="w")

        self.content_box = ScrolledText(
            right,
            wrap=tk.WORD,
            font=("Consolas", 11)
        )
        self.content_box.pack(
            fill="both",
            expand=True,
            pady=(3, 10)
        )

        # Buttons
        buttons = tk.Frame(right)
        buttons.pack(fill="x")

        tk.Button(
            buttons,
            text="New",
            width=12,
            command=self.new_note
        ).pack(side="left", padx=3)

        tk.Button(
            buttons,
            text="Save",
            width=12,
            command=self.save_note
        ).pack(side="left", padx=3)

        tk.Button(
            buttons,
            text="Delete",
            width=12,
            command=self.delete_note
        ).pack(side="left", padx=3)

        tk.Button(
            buttons,
            text="Preview",
            width=12,
            command=self.preview_markdown
        ).pack(side="left", padx=3)

        tk.Button(
            buttons,
            text="Exit",
            width=12,
            command=self.root.destroy
        ).pack(side="right", padx=3)

    # ---------------- LOAD ----------------

    def load_notes(self, search=""):

        self.note_list.delete(0, tk.END)

        self.notes = get_notes(search)

        for note in self.notes:
            title = note[1]
            tags = note[3]

            if tags:
                text = title + " [" + tags + "]"
            else:
                text = title

            self.note_list.insert(
                tk.END,
                text
            )

    # ---------------- SELECT ----------------

    def select_note(self, event=None):

        selected = self.note_list.curselection()

        if not selected:
            return

        index = selected[0]

        if index >= len(self.notes):
            return

        note = self.notes[index]

        self.selected_id = note[0]

        self.title_box.delete(
            0,
            tk.END
        )
        self.title_box.insert(
            0,
            note[1]
        )

        self.content_box.delete(
            "1.0",
            tk.END
        )
        self.content_box.insert(
            "1.0",
            note[2]
        )

        self.tags_box.delete(
            0,
            tk.END
        )
        self.tags_box.insert(
            0,
            note[3] or ""
        )

    # ---------------- NEW ----------------

    def new_note(self):

        self.selected_id = None

        self.title_box.delete(
            0,
            tk.END
        )

        self.tags_box.delete(
            0,
            tk.END
        )

        self.content_box.delete(
            "1.0",
            tk.END
        )

        self.note_list.selection_clear(
            0,
            tk.END
        )

        self.title_box.focus()

    # ---------------- SAVE ----------------

    def save_note(self):

        title = self.title_box.get().strip()

        content = self.content_box.get(
            "1.0",
            tk.END
        ).strip()

        tags = self.tags_box.get().strip()

        if not title:
            messagebox.showwarning(
                "Warning",
                "Please enter a title."
            )
            return

        if not content:
            messagebox.showwarning(
                "Warning",
                "Please enter some content."
            )
            return

        con = sqlite3.connect(DB)

        if self.selected_id is None:

            cursor = con.execute("""
                INSERT INTO notes(title, content, tags)
                VALUES (?, ?, ?)
            """, (title, content, tags))

            self.selected_id = cursor.lastrowid

            message = "Note created successfully."

        else:

            con.execute("""
                UPDATE notes
                SET title = ?, content = ?, tags = ?
                WHERE id = ?
            """, (
                title,
                content,
                tags,
                self.selected_id
            ))

            message = "Note updated successfully."

        con.commit()
        con.close()

        self.load_notes(
            self.search_box.get().strip()
        )

        messagebox.showinfo(
            "Success",
            message
        )

    # ---------------- DELETE ----------------

    def delete_note(self):

        if self.selected_id is None:
            messagebox.showwarning(
                "Warning",
                "Please select a note first."
            )
            return

        answer = messagebox.askyesno(
            "Delete",
            "Delete this note?"
        )

        if not answer:
            return

        con = sqlite3.connect(DB)

        con.execute(
            "DELETE FROM notes WHERE id = ?",
            (self.selected_id,)
        )

        con.commit()
        con.close()

        self.new_note()

        self.load_notes(
            self.search_box.get().strip()
        )

        messagebox.showinfo(
            "Success",
            "Note deleted successfully."
        )

    # ---------------- SEARCH ----------------

    def search_notes(self, event=None):

        search = self.search_box.get().strip()

        self.load_notes(search)

    def clear_search(self):

        self.search_box.delete(
            0,
            tk.END
        )

        self.load_notes()

    # ---------------- MARKDOWN ----------------

    def preview_markdown(self):

        text = self.content_box.get(
            "1.0",
            tk.END
        ).strip()

        if not text:
            messagebox.showwarning(
                "Warning",
                "Enter some Markdown content first."
            )
            return

        try:

            html = markdown.markdown(
                text,
                extensions=[
                    "extra",
                    "fenced_code",
                    "tables"
                ]
            )

            page = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Markdown Preview</title>

<style>
body {
    font-family: Arial, sans-serif;
    max-width: 850px;
    margin: 40px auto;
    padding: 20px;
    line-height: 1.6;
}

pre {
    background: #f4f4f4;
    padding: 15px;
    border-radius: 5px;
}

code {
    background: #f4f4f4;
    padding: 3px;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ccc;
    padding: 8px;
}

th {
    background: #eee;
}
</style>

</head>

<body>
""" + html + """
</body>
</html>
"""

            file = tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                suffix=".html",
                delete=False
            )

            file.write(page)
            file.close()

            webbrowser.open(
                "file://" + os.path.abspath(file.name)
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                "Markdown preview failed:\n" + str(error)
            )


# ---------------- START ----------------

if __name__ == "__main__":

    create_database()

    root = tk.Tk()

    app = NotesApp(root)

    root.mainloop()