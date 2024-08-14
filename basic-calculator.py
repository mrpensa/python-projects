import tkinter as tk
from ttkbootstrap import Style

values_matrix = [
    [1, 2, 3, '+'],
    [4, 5, 6, '-'],
    [7, 8, 9, '*'],
    ['C', 0, '.', '/']
]

def operation(value):
    if value == '=':
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif value == 'C':
        entry_var.set("")
    elif value == 'DEL':
        current_text = entry_var.get()
        entry_var.set(current_text[:-1]) 
    else:
        current_text = entry_var.get()
        entry_var.set(current_text + str(value))

root = tk.Tk()
root.title("Calculator")
style = Style(theme="flatly")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=('Helvetica', 24), justify='right', bd=10)
entry.grid(row=0, column=0, columnspan=4)

buttons = []
for i in range(4):
    row = []
    for j in range(4):
        value = values_matrix[i][j]
        button_text = str(value) if value != '' else ''
        button = tk.Button(root, text=button_text, width=5, height=2, font=('Helvetica', 24),
                           command=lambda v=value: operation(v))
        button.grid(row=i + 1, column=j, padx=5, pady=5)
        row.append(button)
    buttons.append(row)

equal_button = tk.Button(root, text='=', width=10, height=2, font=('Helvetica', 24),
                         command=lambda: operation('='))
equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

del_button = tk.Button(root, text='DEL', width=10, height=2, font=('Helvetica', 24),
                       command=lambda: operation('DEL'))
del_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
