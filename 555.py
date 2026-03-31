import tkinter as tk
from tkinter import messagebox


def vigenere_cipher(text, key, encrypt=True):
    result = ""
    key = key.upper()
    key_index = 0
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    for char in text.upper():
        if char in alphabet:
            char_idx = alphabet.index(char)
            key_char = key[key_index % len(key)]
            key_idx = alphabet.index(key_char)

            if encrypt:
                new_idx = (char_idx + key_idx) % len(alphabet)
            else:
                new_idx = (char_idx - key_idx) % len(alphabet)

            result += alphabet[new_idx]
            key_index += 1
        else:
            result += char
    return result


def process_text(mode):
    text = entry_text.get()
    key = entry_key.get()

    if not key:
        messagebox.showwarning("Ошибка", "Введите ключ!")
        return

    result = vigenere_cipher(text, key, encrypt=(mode == 'encrypt'))
    label_result.config(text=f"Результат: {result}")



root = tk.Tk()
root.title("Шифр Виженера")
root.geometry("400x300")

tk.Label(root, text="Введите текст (RU):").pack(pady=5)
entry_text = tk.Entry(root, width=40)
entry_text.pack()

tk.Label(root, text="Ключевое слово:").pack(pady=5)
entry_key = tk.Entry(root, width=20)
entry_key.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Зашифровать", command=lambda: process_text('encrypt')).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Расшифровать", command=lambda: process_text('decrypt')).pack(side=tk.LEFT, padx=5)

label_result = tk.Label(root, text="Результат: ", wraplength=350)
label_result.pack(pady=10)

root.mainloop()