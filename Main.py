import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import json
import os

current_file_directory = ""

def open_file():
    global current_file_directory
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        current_file_directory = os.path.dirname(file_path)
        with open(file_path, "r") as f:
            data = json.load(f)
            note = data.get("note", "")
            text_box.delete("1.0", "end")
            text_box.insert("1.0", note)
        file_path_entry.delete(0, "end")
        file_path_entry.insert(0, current_file_directory)

def save_note():
    filename = file_name_entry.get()
    file_path = file_path_entry.get()

    if not filename or not file_path:
        messagebox.showerror("Error", "Please enter both filename and path.")
        return

    note = text_box.get("1.0", "end-1c")
    note_data = {"note": note}
    with open(f"{file_path}/{filename}.txt", "w") as f:
        f.write(note)
    messagebox.showinfo("Note Saved", "Your note has been saved successfully.")

# Create main window
root = tk.Tk()
root.title("Modern Note Taker")
root.geometry("400x350")

# Create menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Create text box with scrollbar
text_frame = ttk.Frame(root)
text_frame.pack(fill="both", expand=True)

text_box = tk.Text(text_frame, height=15, width=40, wrap="word")
scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=text_box.yview)
scrollbar.pack(side="right", fill="y")
text_box.pack(side="left", fill="both", expand=True)
text_box.config(yscrollcommand=scrollbar.set)

# Create filename entry
file_name_frame = ttk.Frame(root)
file_name_frame.pack(pady=5)

file_name_label = ttk.Label(file_name_frame, text="Filename:")
file_name_label.pack(side="left")

file_name_entry = ttk.Entry(file_name_frame, width=20)
file_name_entry.pack(side="left")

# Create file path entry
file_path_frame = ttk.Frame(root)
file_path_frame.pack(pady=5)

file_path_label = ttk.Label(file_path_frame, text="File Path:")
file_path_label.pack(side="left")

file_path_entry = ttk.Entry(file_path_frame, width=20)
file_path_entry.pack(side="left")

# Create save button
save_button = ttk.Button(root, text="Save Note", command=save_note)
save_button.pack(pady=10)

# Run the application
root.mainloop()
