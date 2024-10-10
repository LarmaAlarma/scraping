import tkinter as tk
from tkinter import ttk
import csv
import os

class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quote Finder")
        self.root.configure(bg='lightblue')

        self.frame = tk.Frame(root, bg='lightblue')
        self.frame.pack(pady=20)

        self.author_label = tk.Label(self.frame, text="Select Author:", bg='lightblue', font=("Helvetica", 14))
        self.author_label.pack(pady=10)

        self.author_combobox = ttk.Combobox(self.frame, state='readonly')
        self.author_combobox.pack(pady=10)
        self.author_combobox.bind("<<ComboboxSelected>>", self.display_quotes)

        self.quote_text = tk.Text(self.frame, wrap=tk.WORD, height=10, width=50, bg='white', fg='black', font=("Helvetica", 12))
        self.quote_text.pack(pady=10)

        self.load_authors()

    def load_authors(self):
        """Load authors from the CSV file into the combobox."""
        if not os.path.exists('quotes.csv'):
            self.author_combobox['values'] = []
            return

        with open('quotes.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header
            authors = set(row[0] for row in csv_reader if row)  # Using set to avoid duplicates
            self.author_combobox['values'] = sorted(authors)

    def display_quotes(self, event):
        """Display quotes for the selected author."""
        selected_author = self.author_combobox.get()
        self.quote_text.delete(1.0, tk.END)  # Clear previous quotes
        
        with open('quotes.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header
            quotes = [row[1] for row in csv_reader if row and row[0] == selected_author]

            if quotes:
                self.quote_text.insert(tk.END, "\n".join(quotes))
            else:
                self.quote_text.insert(tk.END, "No quotes found for this author.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteApp(root)
    root.mainloop()
