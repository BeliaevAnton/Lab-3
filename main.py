import tkinter as tk
import random
import string


weights = {}

for i, letter in enumerate(string.ascii_uppercase):
    weights[letter] = i + 1

for i, digit in enumerate(string.digits):
    weights[digit] = i + 27

MIN_SUM = 30
MAX_SUM = 35


def generate_block():
    while True:
        block = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        total = sum(weights[c] for c in block)
        if MIN_SUM <= total <= MAX_SUM:
            return block


def generate_key():
    return "-".join(generate_block() for _ in range(3))



def on_generate():
    key = generate_key()
    entry.delete(0, tk.END)
    entry.insert(0, key)


root = tk.Tk()
root.title("KeyGen Variant 4")
root.geometry("500x300")

entry = tk.Entry(root, font=("Consolas", 20), justify="center")
entry.pack(pady=40)

button = tk.Button(root, text="Generate Key", command=on_generate)
button.pack(pady=20)

root.mainloop()