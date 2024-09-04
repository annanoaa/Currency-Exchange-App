import tkinter as tk
from tkinter import ttk
from tkinter import font

from django.views.decorators.csrf import requires_csrf_token

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

#create amount input field
amount_label = ttk.Label(root, background="lightblue", font = large_font, text="Amount:")
amount_label.grid(column=0, row=0, padx=15, pady=15)
amount_var = tk.StringVar()
amount_entry = ttk.Entry(root, textvariable=amount_var, font=('calibre',14,'normal'))
amount_entry.grid(column=1, row=0, padx=15, pady=15)


#create from currency field
fromCurrency_label = ttk.Label(root, background="lightblue", font = large_font, text="From Currency:")
fromCurrency_label.grid(column=0, row=1, padx=15, pady=15)
fromCurrency_var = tk.StringVar(value="GEL")
fromCurrency_option = ttk.OptionMenu(root, fromCurrency_var, "GEL", *conversion_rates.keys())
fromCurrency_option.grid(column=0, row=2, padx=15, pady=15)

#create to currency field
toCurrency_label = ttk.Label(root, background="lightblue", font = large_font, text="To Currency:")
toCurrency_label.grid(column=1, row=1, padx=15, pady=15)
toCurrency_var = tk.StringVar(value="USD")
toCurrency_option = ttk.OptionMenu(root, toCurrency_var,"USD", *conversion_rates.keys())
toCurrency_option.grid(column=1, row=2, padx=15, pady=15)

#create result field
result_var = tk.StringVar()
result_label = ttk.Label(root, background="lightblue", font = large_font, text="Converted amount:", textvariable=result_var)
result_label.grid(column=0, row=3, columnspan=2, padx=15, pady=15)


#create convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency, font=("Arial", 12),
                   height=2, relief="raised", width=8)
convert_button.grid(column=0, row=4, padx=15, pady=15)

#create clear button
clear_button = tk.Button(root, text="Clear", command=clear, font=("Arial", 12),
                   height=2, relief="raised", width=8)
clear_button.grid(column=1, row=4,  padx=15, pady=15)


root.mainloop()