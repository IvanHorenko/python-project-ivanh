import random
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def generuj():
    try:
        N = int(entry_n.get())
    except:
        messagebox.showerror("Chyba", "Pole N musí byť celé číslo.")
        return

    try:
        K = float(entry_k.get())
    except:
        messagebox.showerror("Chyba", "Pole K musí byť číslo.")
        return

    if N <= 1:
        messagebox.showerror("Chyba", "N musí byť väčšie než 1.")
        return

    numbers = [random.randint(0, 100) for _ in range(N)]
    diffs = [numbers[i+1] - numbers[i] for i in range(N-1)]
    adjusted = [d + K for d in diffs]

    lb_orig.delete(0, tk.END)
    for i, v in enumerate(numbers):
        lb_orig.insert(tk.END, f"{i}: {v}")

    lb_diff.delete(0, tk.END)
    for i, v in enumerate(adjusted):
        lb_diff.insert(tk.END, f"{i}: {v}")

    ax.clear()
    ax.set_title("Rozdiely medzi susedmi + K", fontsize=12)
    ax.set_xlabel("Index (i)", fontsize=10)
    ax.set_ylabel("Hodnota rozdielu + K", fontsize=10)

    ax.plot(range(len(adjusted)), adjusted, marker="o")
    ax.grid(True)

    fig.tight_layout()
    canvas.draw_idle()


root = tk.Tk()
root.title("Rozdiely medzi číslami")
root.geometry("1000x720")
root.resizable(False, False)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

ttk.Label(root, text="N (počet čísel):").grid(row=0, column=0, sticky="ew", padx=5, pady=5)
entry_n = ttk.Entry(root, width=15)
entry_n.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
entry_n.insert(0, "10")

ttk.Label(root, text="K (pripočítať):").grid(row=1, column=0, sticky="ew", padx=5, pady=5)
entry_k = ttk.Entry(root, width=15)
entry_k.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
entry_k.insert(0, "0")

ttk.Button(root, text="Generovať", command=generuj).grid(
    row=2, column=0, columnspan=2, pady=10, sticky="ew"
)

ttk.Label(root, text="Pôvodné čísla").grid(row=3, column=0, pady=5, sticky="ew")
ttk.Label(root, text="Rozdiely + K").grid(row=3, column=1, pady=5, sticky="ew")

lb_orig = tk.Listbox(root, width=30, height=12)
lb_orig.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

lb_diff = tk.Listbox(root, width=30, height=12)
lb_diff.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

fig, ax = plt.subplots(figsize=(6, 3.5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

root.mainloop()