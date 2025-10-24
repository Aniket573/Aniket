import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for char in row:
        btn = tk.Button(frame, text=char, font="Arial 18", relief=tk.RAISED, border=1)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", click)

# Run the GUI loop
root.mainloop()
