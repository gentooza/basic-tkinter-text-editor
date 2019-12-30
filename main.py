import tkinter as tk
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText
import file_menu
import edit_menu
import format_menu
import help_menu

root = tk.Tk()

root.title("Text Editor-Untiltled")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

font = Font(family="Verdana", size=10)

text = ScrolledText(root, state='normal',
                    height=400, width=400,
                    wrap='word',
                    font=font, pady=2,
                    padx=3, undo=True)
text.pack(fill=tk.Y, expand=1)
text.focus_set()

menubar = tk.Menu(root)

file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, text, menubar)
root.mainloop()
