import tkinter as tk
from tkinter import ttk
from tkinter import font

# Define conversion rates
conversion_rates = {
    "GEL": {"GEL": 1.0, "USD": 0.37, "EUR": 0.34, "GBP": 0.28},
    "USD": {"GEL": 2.69, "USD": 1.0, "EUR": 0.91, "GBP": 0.76},
    "EUR": {"GEL": 2.97, "USD": 1.1, "EUR": 1.0, "GBP": 0.84},
    "GBP": {"GEL": 3.53, "USD": 1.31, "EUR": 1.19, "GBP": 1.0}
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
root.geometry("550x400")

large_font = font.Font(family="Helvetica", size=14, weight="bold")

# Create frames
amount_frame = ttk.Frame(root)
amount_frame.grid(column=0, row=0, padx=15, pady=15, columnspan=2)

currency_frame = ttk.Frame(root)
currency_frame.grid(column=0, row=1, padx=15, pady=15, columnspan=2)

result_frame = ttk.Frame(root)
result_frame.grid(column=0, row=2, padx=15, pady=15, columnspan=2)

button_frame = ttk.Frame(root)
button_frame.grid(column=0, row=3, padx=15, pady=15, columnspan=2)

# Set the background color of the frames
amount_frame.configure(style="TFrame")
currency_frame.configure(style="TFrame")
result_frame.configure(style="TFrame")
button_frame.configure(style="TFrame")

style = ttk.Style()
style.configure("TFrame", background="lightblue")

# Amount input field
amount_label = ttk.Label(amount_frame, background="lightblue", font=large_font, text="Amount:")
amount_label.grid(column=0, row=0, padx=15, pady=15)
amount_var = tk.StringVar()
amount_entry = ttk.Entry(amount_frame, textvariable=amount_var, font=('calibre', 14, 'normal'))
amount_entry.grid(column=1, row=0, padx=15, pady=15)

# From currency field
fromCurrency_label = ttk.Label(currency_frame, background="lightblue", font=large_font, text="From Currency:")
fromCurrency_label.grid(column=0, row=0, padx=15, pady=15)
fromCurrency_var = tk.StringVar(value="GEL")
fromCurrency_option = ttk.OptionMenu(currency_frame, fromCurrency_var, "GEL", *conversion_rates.keys())
fromCurrency_option.grid(column=1, row=0, padx=15, pady=15)

# To currency field
toCurrency_label = ttk.Label(currency_frame, background="lightblue", font=large_font, text="To Currency:")
toCurrency_label.grid(column=2, row=0, padx=15, pady=15)
toCurrency_var = tk.StringVar(value="USD")
toCurrency_option = ttk.OptionMenu(currency_frame, toCurrency_var, "USD", *conversion_rates.keys())
toCurrency_option.grid(column=3, row=0, padx=15, pady=15)

# Result field
result_label = ttk.Label(result_frame, background="lightblue", font=large_font)
result_label.grid(column=0, row=0, padx=15, pady=15)
result_var = tk.StringVar()
result_display = ttk.Label(result_frame, background="lightblue", font=large_font, textvariable=result_var)
result_display.grid(column=1, row=0, padx=15, pady=15)

# Convert and Clear buttons
convert_button = tk.Button(button_frame, text="Convert", command=convert_currency, font=("Arial", 12),
                           height=2, relief="raised", width=8)
convert_button.grid(column=0, row=0, padx=15, pady=15)

clear_button = tk.Button(button_frame, text="Clear", command=clear, font=("Arial", 12),
                         height=2, relief="raised", width=8)
clear_button.grid(column=1, row=0, padx=15, pady=15)

root.mainloop()
