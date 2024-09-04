import tkinter as tk
from tkinter import ttk
from tkinter import font

# Define conversion rates
conversion_rates = {
    "GEL": {"GEL": 1.0, "USD": 0.37, "EUR": 0.34, "GBP": 0.28},
    "USD": {"GEL": 2.69, "USD": 1.0, "EUR": 0.92, "GBP": 0.78,},
    "EUR": {"GEL": 2.9, "USD": 1.09, "EUR": 1.0, "GBP": 0.85},
    "GBP": {"GEL": 3.45, "USD": 1.28, "EUR": 1.18, "GBP": 1.0}
}

def convert_currency():
    from_currency = fromCurrency_var.get()
    to_currency = toCurrency_var.get()
    amount = amount_var.get()

    if not amount:
        result_var.set("Please enter an amount.")
        return

    try:
        amount = float(amount)
        converted_amount = amount * conversion_rates[from_currency][to_currency]
        result_var.set(f"{converted_amount:.2f} {to_currency}")
    except ValueError:
        result_var.set("Invalid input. Please enter a numeric value.")

def clear():
    amount_var.set("")
    result_var.set("")
    fromCurrency_var.set("GEL")
    toCurrency_var.set("USD")

# Create the main window
root = tk.Tk()
root.title("Currency Exchange Rate Calculator")
root.configure(bg="lightblue")
root.geometry("450x300")

large_font = font.Font(family="Helvetica", size=14, weight="bold")

# Configure grid weights to allow resizing
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

# Create frames
amount_frame = ttk.Frame(root)
amount_frame.grid(column=0, row=0, padx=15, pady=15, columnspan=2, sticky="nsew")

currency_frame = ttk.Frame(root)
currency_frame.grid(column=0, row=1, padx=15, pady=15, columnspan=2, sticky="nsew")

result_frame = ttk.Frame(root)
result_frame.grid(column=0, row=2, padx=15, pady=15, columnspan=2, sticky="nsew")

button_frame = ttk.Frame(root)
button_frame.grid(column=0, row=3, padx=15, pady=15, columnspan=2, sticky="nsew")

# Set the background color of the frames
amount_frame.configure(style="TFrame")
currency_frame.configure(style="TFrame")
result_frame.configure(style="TFrame")
button_frame.configure(style="TFrame")

style = ttk.Style()
style.configure("TFrame", background="lightblue")

# Configure frame grid weights
amount_frame.grid_columnconfigure(0, weight=1)
amount_frame.grid_columnconfigure(1, weight=1)
currency_frame.grid_columnconfigure(0, weight=1)
currency_frame.grid_columnconfigure(1, weight=1)
currency_frame.grid_columnconfigure(2, weight=1)
currency_frame.grid_columnconfigure(3, weight=1)
result_frame.grid_columnconfigure(0, weight=1)
result_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

# Amount input field
amount_label = ttk.Label(amount_frame, background="lightblue", font=large_font, text="Amount:")
amount_label.grid(column=0, row=0, padx=15, pady=15, sticky="w")
amount_var = tk.StringVar()
amount_entry = ttk.Entry(amount_frame, textvariable=amount_var, font=('calibre', 14, 'normal'))
amount_entry.grid(column=1, row=0, padx=15, pady=15, sticky="ew")

# From currency field
fromCurrency_label = ttk.Label(currency_frame, background="lightblue", font=large_font, text="From Currency:")
fromCurrency_label.grid(column=0, row=0, padx=15, pady=15, sticky="e")
fromCurrency_var = tk.StringVar(value="GEL")
fromCurrency_option = ttk.OptionMenu(currency_frame, fromCurrency_var, "GEL", *conversion_rates.keys())
fromCurrency_option.grid(column=1, row=0, padx=15, pady=15, sticky="ew")

# To currency field
toCurrency_label = ttk.Label(currency_frame, background="lightblue", font=large_font, text="To Currency:")
toCurrency_label.grid(column=2, row=0, padx=15, pady=15, sticky="e")
toCurrency_var = tk.StringVar(value="USD")
toCurrency_option = ttk.OptionMenu(currency_frame, toCurrency_var, "USD", *conversion_rates.keys())
toCurrency_option.grid(column=3, row=0, padx=15, pady=15, sticky="ew")

# Result field
result_label = ttk.Label(result_frame, background="lightblue", font=large_font, text="Converted amount:")
result_label.grid(column=0, row=0, padx=15, pady=15, sticky="w")
result_var = tk.StringVar()
result_display = ttk.Label(result_frame, background="lightblue", font=large_font, textvariable=result_var)
result_display.grid(column=1, row=0, padx=15, pady=15, sticky="ew")

# Convert and Clear buttons
convert_button = tk.Button(button_frame, text="Convert", command=convert_currency, font=("Arial", 12),
                           height=2, relief="raised", width=8)
convert_button.grid(column=0, row=0, padx=15, pady=15, sticky="ew")

clear_button = tk.Button(button_frame, text="Clear", command=clear, font=("Arial", 12),
                         height=2, relief="raised", width=8)
clear_button.grid(column=1, row=0, padx=15, pady=15, sticky="ew")

root.mainloop()
