
import tkinter as tk
from tkinter import messagebox

def write_to_file(file_path, content, mode='w'):
    """
    Write or append content to a file.

    Parameters:
    - file_path (str): The full path including the drive letter (e.g., 'D:/path/to/your/file.txt').
    - content (str): The content to write or append to the file.
    - mode (str): The file open mode ('w' for write, 'a' for append). Default is 'w'.
    """
    with open(file_path, mode) as file:
        file.write(content)

def read_and_display_file(file_path):
    """
    Read and display the content of a file in a message box.

    Parameters:
    - file_path (str): The full path including the drive letter.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            messagebox.showinfo("File Content", content)
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found at {file_path}")


if __name__ == "__main__":
    # Example usage when the script is run as the main program
    file_path = 'c:/Enron/_Prv/_Szkolenia/_Praktyka/REPO/TEST/data/example.txt'

    # Write to the file
    write_to_file(file_path, 'Hello, this is a sample text.\nWriting to a file in Python is easy!')

    # Read and display the content of the file
    read_and_display_file(file_path)

    # To append content:
    write_to_file(file_path, '\nThis line is appended to the existing content.', mode='a')

    # Read and display the updated content of the file
    read_and_display_file(file_path)






