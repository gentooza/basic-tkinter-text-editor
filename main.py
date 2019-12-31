#!/usr/bin/env python3
'''
Copyright (C) 2015 Punith Patil
Copyright (C) 2019-2020 Joaquín Cuéllar

This file is part of Basic Simple Text Editor.

Basic Simple Text Editor is free software:
you can redistribute it and/or modify it under the terms of
the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Basic Simple Text Editor is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Basic Simple Text Editor.
If not, see <https://www.gnu.org/licenses/>.
'''

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
