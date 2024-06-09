import tkinter as tk
from tkinter import ttk

def calculate_combinations():
    coin_values = coin_entry.get().split(',')
    coin_values = [int(coin.strip()) for coin in coin_values]
    target_amount = int(amount_entry.get())
    result = []
    
    coin_values.sort(reverse=True)

    original_target = target_amount 
    for coin in coin_values:
        if coin == 0:
            break
        else:
            while target_amount >= coin:
                target_amount -= coin
                result.append(coin)
        
    # Clear the result text area
    result_text.delete(1.0, tk.END)
    
    # Check if there is any leftover amount (indicating no solution)
    if target_amount != 0:
        result_text.insert(tk.END, f"Tidak ada kombinasi koin yang memenuhi jumlah {original_target} dengan koin yang diberikan.\n")
    else:
        result_text.insert(tk.END, f"Kombinasi koin untuk jumlah {original_target} adalah: {result}\n")

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
result_text = tk.Text(mainframe, width=60, height=20)
result_text.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

# Configure grid
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
