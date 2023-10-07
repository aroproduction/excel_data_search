import pandas as pd
import tkinter as tk
from tkinter import ttk

# Load the Excel data into a Pandas DataFrame
# df = pd.read_excel('records.csv')
df = pd.read_excel('./problemStatements.xlsx')

# Create a serial number column
df.insert(0, 'Serial No.', range(1, len(df) + 1))

# Create a function to perform the search
def search(event=None):
    keyword = entry.get().strip()  # Get the search keyword from the user input
    if keyword:
        # Perform the search based on the chosen column
        result = df[df[search_var.get()].astype(str).str.contains(keyword, case=False)]

        # Display the search results in the treeview widget
        clear_treeview()
        for index, row in result.iterrows():
            treeview.insert('', 'end', values=row.tolist())
    else:
        # Display the full table if the search box is empty
        clear_treeview()
        for index, row in df.iterrows():
            treeview.insert('', 'end', values=row.tolist())

# Create a function to clear the treeview widget
def clear_treeview():
    for i in treeview.get_children():
        treeview.delete(i)

# Create the main application window
root = tk.Tk()
root.title("Excel Data Search Application")

# Create a search frame
search_frame = ttk.Frame(root)
search_frame.pack(pady=10)

# Create and set a search label and entry
search_label = ttk.Label(search_frame, text="Search Keyword:")
search_label.grid(row=0, column=0, padx=10, pady=5)
entry = ttk.Entry(search_frame)
entry.grid(row=0, column=1, padx=10, pady=5)

# Bind the search function to the KeyRelease event of the entry widget
entry.bind('<KeyRelease>', search)

# Create a combobox for selecting search columns
search_var = tk.StringVar()
search_combobox = ttk.Combobox(search_frame, textvariable=search_var, values=list(df.columns))
search_combobox.grid(row=0, column=2, padx=10, pady=5)
search_combobox.set("ID")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Create a treeview widget to display search results
columns = df.columns.tolist()
treeview = ttk.Treeview(frame, columns=columns, show='headings')
col_widths = [30] + [40, 180, 95, 50, 190, 70, 70]  # Serial No. column width added
for col, wd in zip(columns, col_widths):
    treeview.heading(col, text=col)
    treeview.column(col, anchor='center', width=wd)
treeview.pack(side=tk.LEFT, fill="both", expand=True)

# Create a vertical scrollbar
vsb = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=vsb.set)
vsb.pack(side=tk.RIGHT, fill=tk.Y)

# Display the full table initially
for index, row in df.iterrows():
    treeview.insert('', 'end', values=row.tolist())

# Start the GUI main loop
root.mainloop()
