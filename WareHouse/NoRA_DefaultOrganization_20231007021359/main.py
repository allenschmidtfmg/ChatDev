'''
This is the main file of the software. It initializes the GUI and handles user interactions.
'''
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from object_manager import ObjectManager
from note_manager import NoteManager
from database import Database
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Object Manager")
        self.geometry("800x600")
        self.object_manager = ObjectManager()
        self.note_manager = NoteManager()
        self.database = Database()
        self.create_menu()
        self.create_note_section()
        self.create_object_section()
    def create_menu(self):
        # Create menu bar and options
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save Objects", command=self.save_objects)
        file_menu.add_command(label="Load Objects", command=self.load_objects)
        file_menu.add_separator()
        file_menu.add_command(label="Save Notes", command=self.save_notes)
        file_menu.add_command(label="Load Notes", command=self.load_notes)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
    def create_note_section(self):
        # Create note section GUI
        note_frame = tk.Frame(self)
        note_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        note_label = tk.Label(note_frame, text="Notes")
        note_label.pack()
        self.note_listbox = tk.Listbox(note_frame)
        self.note_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        note_scrollbar = tk.Scrollbar(note_frame)
        note_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.note_listbox.config(yscrollcommand=note_scrollbar.set)
        note_scrollbar.config(command=self.note_listbox.yview)
        note_button_frame = tk.Frame(note_frame)
        note_button_frame.pack()
        add_note_button = tk.Button(note_button_frame, text="Add Note", command=self.add_note)
        add_note_button.pack(side=tk.LEFT)
        delete_note_button = tk.Button(note_button_frame, text="Delete Note", command=self.delete_note)
        delete_note_button.pack(side=tk.LEFT)
    def create_object_section(self):
        # Create object section GUI
        object_frame = tk.Frame(self)
        object_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        object_label = tk.Label(object_frame, text="Objects")
        object_label.pack()
        self.object_listbox = tk.Listbox(object_frame)
        self.object_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        object_scrollbar = tk.Scrollbar(object_frame)
        object_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.object_listbox.config(yscrollcommand=object_scrollbar.set)
        object_scrollbar.config(command=self.object_listbox.yview)
        object_button_frame = tk.Frame(object_frame)
        object_button_frame.pack()
        add_object_button = tk.Button(object_button_frame, text="Add Object", command=self.add_object)
        add_object_button.pack(side=tk.LEFT)
        delete_object_button = tk.Button(object_button_frame, text="Delete Object", command=self.delete_object)
        delete_object_button.pack(side=tk.LEFT)
    def add_object(self):
        # Add a new object to the list
        object_name = simpledialog.askstring("Add Object", "Enter the object name:")
        if object_name:
            self.object_manager.add_object(object_name)
            self.object_listbox.insert(tk.END, object_name)
    def delete_object(self):
        # Delete an object from the list
        selected_index = self.object_listbox.curselection()
        if selected_index:
            object_name = self.object_listbox.get(selected_index)
            self.object_manager.delete_object(object_name)
            self.object_listbox.delete(selected_index)
    def save_objects(self):
        # Save the list of objects to the database
        self.object_manager.save_objects()
        messagebox.showinfo("Save Objects", "Objects saved successfully.")
    def load_objects(self):
        # Load the list of objects from the database
        self.object_manager.load_objects()
        self.object_listbox.delete(0, tk.END)
        for obj in self.object_manager.get_objects():
            self.object_listbox.insert(tk.END, obj)
    def add_note(self):
        # Add a new note to the note section
        note = simpledialog.askstring("Add Note", "Enter a new note:")
        if note:
            self.note_manager.add_note(note)
            self.note_listbox.insert(tk.END, note)
    def delete_note(self):
        # Delete a note from the note section
        selected_index = self.note_listbox.curselection()
        if selected_index:
            note = self.note_listbox.get(selected_index)
            self.note_manager.delete_note(note)
            self.note_listbox.delete(selected_index)
    def save_notes(self):
        # Save the notes to the database
        self.note_manager.save_notes()
        messagebox.showinfo("Save Notes", "Notes saved successfully.")
    def load_notes(self):
        # Load the notes from the database
        self.note_manager.load_notes()
        self.note_listbox.delete(0, tk.END)
        for note in self.note_manager.get_notes():
            self.note_listbox.insert(tk.END, note)
if __name__ == "__main__":
    app = Application()
    app.mainloop()