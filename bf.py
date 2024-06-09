import tkinter as tk
from tkinter import ttk

def find_combinations(coins, target):
    all_combinations = []
    stack = [(0, [], target)]

    while stack:
        start_index, current_combination, current_target = stack.pop()

        if current_target == 0:
            all_combinations.append(current_combination[:])
            continue

        for i in range(start_index, len(coins)):
            coin = coins[i]
            if coin <= current_target:
                new_combination = current_combination + [coin]
                new_target = current_target - coin
                stack.append((i, new_combination, new_target))

    return all_combinations

def calculate_combinations():
    coin_values = coin_entry.get().split(',')
    coin_values = [int(coin.strip()) for coin in coin_values]
    target_amount = int(amount_entry.get())
    
    all_combinations = find_combinations(coin_values, target_amount)
    
    result_text.delete(1.0, tk.END)
    if not all_combinations:
        result_text.insert(tk.END, "Tidak ada kombinasi yang ditemukan.\n")
    else:
        for combination in all_combinations:
            result_text.insert(tk.END, f"{combination}\n")

# Setup GUI
root = tk.Tk()
root.title("Coin Change Problem Solver")

mainframe = ttk.Frame(root, padding="10 10 20 20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Coin entry
ttk.Label(mainframe, text="Masukkan nilai koin (dipisahkan dengan koma):").grid(column=1, row=1, sticky=tk.W)
coin_entry = ttk.Entry(mainframe, width=40)
coin_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

# Amount entry
ttk.Label(mainframe, text="Masukkan jumlah uang yang akan ditukar:").grid(column=1, row=2, sticky=tk.W)
amount_entry = ttk.Entry(mainframe, width=40)
amount_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

# Calculate button
calculate_button = ttk.Button(mainframe, text="Hitung Kombinasi", command=calculate_combinations)
calculate_button.grid(column=2, row=3, sticky=tk.W)

# Result text area
result_text = tk.Text(mainframe, width=100, height=150)
result_text.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

# Configure grid
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
