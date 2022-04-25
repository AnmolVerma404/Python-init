import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.withdraw()

messagebox.showerror("Error","Error message")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Information message")