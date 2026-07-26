import tkinter as tk
from tkinter import filedialog, messagebox

from organizer import organize_files


def create_window():

    root = tk.Tk()
    root.title("Smart Download Organizer")
    root.geometry("450x300")


    folder_path = ""


    def select_folder():
        nonlocal folder_path

        folder_path = filedialog.askdirectory()

        if folder_path:
            path_label.config(text=folder_path)



    def organize():

        if folder_path:

            result = organize_files(folder_path)

            if result:
                messagebox.showinfo(
                    "Done",
                    "Files organized successfully!"
                )

        else:
            messagebox.showwarning(
                "Warning",
                "Please select a folder first"
            )



    title = tk.Label(
        root,
        text="Smart Download Organizer",
        font=("Arial", 16)
    )
    title.pack(pady=20)



    select_button = tk.Button(
        root,
        text="Select Folder",
        command=select_folder
    )
    select_button.pack()



    path_label = tk.Label(
        root,
        text="No folder selected"
    )
    path_label.pack(pady=20)



    organize_button = tk.Button(
        root,
        text="Organize",
        command=organize
    )
    organize_button.pack()



    root.mainloop()