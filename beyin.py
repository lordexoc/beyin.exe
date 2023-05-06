import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import time


def guess_number():
    input_number = input_box.get()
    progress_window = tk.Toplevel(root)
    progress_window.geometry("500x200")
    progress_label = tk.Label(progress_window, text="Beynini Okuyorum...")
    progress_label.pack(pady=10)
    progress_bar = tk.ttk.Progressbar(progress_window, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=10)

    for i in range(11):
        progress_bar["value"] = i * 10
        progress_window.update_idletasks()
        time.sleep(1)
        if i == 2:
            progress_label.config(text="Beyin Dalgaların Okunuyor")
        elif i == 5:
            progress_label.config(text="....Aklından Sayıyı Geçir....")
        elif i == 8:
            progress_label.config(text="................Kolaydın..............")
        
    mb.showinfo("Tahmin Edilen Sayı", f"Beynini okudum ve tuttuğun sayı: {input_number}")
    mb.showinfo("Girilen Sayı", f"Beni takip et by @tanrisopasi")

root = tk.Tk()
root.geometry("400x250")
root.title("Beyin Okuma Programı")

label = tk.Label(root, text="Ben Aklındaki Sayıyı Bulabilirim, Beyin Okuyabiliyorum", font=("Helvetica", 12))
label.pack(pady=10)

input_box = tk.Entry(root)
input_box.pack(pady=10)

input_label = tk.Label(root, text="Aklındaki Sayıyı Buraya Yaz", font=("Helvetica", 10))
input_label.pack(pady=5)

button = tk.Button(root, text="Sayıyı Tahmin Et", command=guess_number)
button.pack()

root.mainloop()
