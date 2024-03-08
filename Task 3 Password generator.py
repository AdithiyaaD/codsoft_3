import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_and_display_password():
    length = int(length_entry.get())
    if length <= 0:
        password_label.config(text="Length must be greater than zero.")
        return
    password = generate_password(length)
    password_label.config(text="Generated Password: " + password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter the desired length of the password:", font=('Times', 25))
length_label.pack()

length_entry = tk.Entry(root, width=50, font=('Times 25'))
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, font=('Times', 25))
generate_button.pack()

password_label = tk.Label(root, text="", font=('Times', 25))
password_label.pack()

root.mainloop()
