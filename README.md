# 📝 Notes Application

A simple and user-friendly **Notes Application** built with **Python 🐍**, **Tkinter 🖥️**, **SQLite 🗄️**, and **Markdown ✍️**.

Create, edit, delete, organize, and search your notes easily from a desktop interface.

---

## ✨ Features

* 📝 **Create Notes** — Create and save new notes
* ✏️ **Edit Notes** — Update existing notes
* 🗑️ **Delete Notes** — Remove unwanted notes
* 📋 **Markdown Support** — Write notes using Markdown syntax
* 👀 **Markdown Preview** — Preview formatted Markdown content
* 🏷️ **Tags** — Organize notes using tags
* 🔍 **Search** — Search notes by title, content, or tags
* 💾 **SQLite Database** — Store notes permanently
* 🕐 **Date & Time Tracking** — Track when notes are created and updated
* 🖥️ **GUI Interface** — Easy-to-use desktop application

---

## 🛠️ Technologies Used

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| 🐍 Python          | Main programming language |
| 🖥️ Tkinter        | Graphical User Interface  |
| 🗄️ SQLite         | Database                  |
| ✍️ Markdown        | Note formatting           |
| 📦 Python-Markdown | Markdown processing       |

---

## 📂 Project Structure

```text
📁 notes-app/
│
├── 🐍 app.py
├── 📦 requirements.txt
├── 📖 README.md
└── 🗄️ notes.db
```

> 💡 `notes.db` is automatically created when you run the application for the first time.

---

## 🚀 Installation

### 1️⃣ Clone or Download the Project

Download the project files and open the project folder in your terminal.

### 2️⃣ Check Python

Make sure Python 3 is installed:

```bash
python --version
```

Recommended: **Python 3.9+** 🐍

### 3️⃣ Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

On some systems:

```bash
pip3 install -r requirements.txt
```

---

## ▶️ Run the Application

Start the application with:

```bash
python app.py
```

🎉 The Notes Application window will open.

---

## 📝 Creating a Note

1. Click **➕ New Note**
2. Enter a title
3. Add tags
4. Write your note
5. Click **💾 Save Note**

### ✍️ Example Markdown

````markdown
# 🐍 Python Notes

## Variables

Python variables are used to store data.

### Example

```python
name = "John"
age = 20
````

**Python is easy to learn!** 🎉

````

---

## 🏷️ Using Tags

Enter tags separated by commas:

```text
python, programming, college, project
````

The application automatically:

* 🔤 Converts tags to lowercase
* 🧹 Removes unwanted characters
* ♻️ Removes duplicate tags

For example:

```text
Python, python, Programming
```

becomes:

```text
python, programming
```

---

## 🔍 Searching Notes

Use the 🔍 **Search** box at the top of the application.

The search feature checks:

* 📝 Note title
* 📄 Note content
* 🏷️ Note tags

For example, searching for:

```text
python
```

will find notes containing `python` in their title, content, or tags.

---

## ✏️ Editing a Note

1. Select a note from the notes list.
2. Change the title, tags, or content.
3. Click **💾 Save Note**.

The application automatically updates the 🕐 modification date.

---

## 🗑️ Deleting a Note

1. Select the note you want to delete.
2. Click **🗑️ Delete Note**.
3. Confirm the deletion.

⚠️ Deleted notes cannot be recovered.

---

## 👀 Markdown Preview

Write Markdown in the editor and click:

```text
👀 Preview Markdown
```

The application will process the Markdown and display a formatted preview.

---

## 💾 Database

The application uses **SQLite** to store notes.

The database file is:

```text
🗄️ notes.db
```

### Database Fields

| Field           | Description               |
| --------------- | ------------------------- |
| 🔢 `id`         | Unique note ID            |
| 📝 `title`      | Note title                |
| 📄 `content`    | Markdown content          |
| 🏷️ `tags`      | Note tags                 |
| 📅 `created_at` | Creation date and time    |
| 🔄 `updated_at` | Last update date and time |

---



Install the Python dependency using:

```bash
pip install -r requirements.txt

---

## 🎯 Future Improvements

The project can be expanded with:

* 🌙 Dark Mode
* 📌 Pin Important Notes
* ❤️ Favorite Notes
* 📁 Categories and Folders
* 📤 Export Notes to PDF
* 📄 Export Notes to Markdown
* 📥 Import Markdown Files
* 🖼️ Image Attachments
* ☁️ Cloud Synchronization
* 🔐 User Authentication
* 💾 Automatic Backups
* 🎨 Improved Markdown Editor
* 🌐 Web Version

---

## 🎓 Project Purpose

This project is useful for learning:

* 🐍 Python programming
* 🖥️ GUI development with Tkinter
* 🗄️ Database management with SQLite
* 🔄 CRUD operations
* 🔍 Search functionality
* 🏷️ Data organization using tags
* ✍️ Markdown processing
* 📦 Python package management

---

## 📸 Application Preview

Add screenshots of your application here:

```text
📷 Screenshot 1 — Main Window
📷 Screenshot 2 — Creating a Note
📷 Screenshot 3 — Markdown Preview
📷 Screenshot 4 — Searching Notes
```

---

## 🤝 Contributing

Contributions are welcome! 🎉

If you would like to improve this project:

1. 🍴 Fork the repository
2. 🌿 Create a new branch
3. ✏️ Make your changes
4. 💾 Commit your changes
5. 🚀 Create a Pull Request

---

## 📄 License

This project is created for **educational purposes 🎓**.

You are free to modify and improve the project for your own learning and development.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

**Made with ❤️ and Python 🐍**

