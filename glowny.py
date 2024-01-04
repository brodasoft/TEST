import tkinter as tk
from tkinter import filedialog

def save_to_file(content):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(content)
        tk.messagebox.showinfo("Success", "Text saved to file successfully!")

def get_text_input():
    text_input = entry.get("1.0", "end-1c")  # Get text from the Text widget
    save_to_file(text_input)

# GUI setup
root = tk.Tk()
root.title("Text Saver")

# Text Entry
entry = tk.Text(root, height=10, width=40)
entry.pack(pady=10)

# Save Button
save_button = tk.Button(root, text="Save Text to File", command=get_text_input)
save_button.pack()

# Run the GUI
root.mainloop()