import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry for entering the amount
        amount_entry = ttk.Entry(self.root, textvariable=self.amount_var, width=15)
        amount_entry.grid(row=0, column=0, padx=10, pady=10)

        # Dropdown for selecting the 'from' currency
        from_currency_combobox = ttk.Combobox(
            self.root,
            textvariable=self.from_currency_var,
            values=self.get_currency_list(),
            state="readonly",
        )
        from_currency_combobox.grid(row=0, column=1, padx=10, pady=10)
        from_currency_combobox.set("USD")  # Set default currency

        # Label for the 'to' currency
        to_currency_label = ttk.Label(self.root, text="To Currency:")
        to_currency_label.grid(row=1, column=0, padx=10, pady=10)

        # Dropdown for selecting the 'to' currency
        to_currency_combobox = ttk.Combobox(
            self.root,
            textvariable=self.to_currency_var,
            values=self.get_currency_list(),
            state="readonly",
        )
        to_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
        to_currency_combobox.set("EUR")  # Set default currency

        # Button to perform the conversion
        convert_button = ttk.Button(
            self.root, text="Convert", command=self.convert_currency
        )
        convert_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Label to display the result
        result_label = ttk.Label(self.root, textvariable=self.result_var)
        result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def convert_currency(self):
        amount = self.amount_var.get()
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()

        c = CurrencyRates()
        rate = c.get_rate(from_currency, to_currency)
        result = f"{amount} {from_currency} = {round(amount * rate, 2)} {to_currency}"

        self.result_var.set(result)

    @staticmethod
    def get_currency_list():
        # You can modify this list to include more currencies
        return ["USD", "EUR", "GBP", "JPY", "INR", "AUD", "CAD", "SGD", "NZD"]


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
