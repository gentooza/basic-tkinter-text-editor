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
import my_globals
import tkinter as tk
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText
import file_menu
import edit_menu
import format_menu
import help_menu


class main_window:

    def __init__(self, master=None): 
        self.master = master
        self.set_app_title(None)
        self.font = Font(family="Verdana", size=10)

        self.text = ScrolledText(self.master, state='normal',
                                 height=400, width=400,
                                 wrap='word',
                                 font=self.font, pady=2,
                                 padx=3, undo=True)
        self.text.pack(fill=tk.Y, expand=1)
        self.text.focus_set()
        self.menubar = tk.Menu(self.master)

    def build(self):
        file_menu.main(self.master, self, self.text, self.menubar)
        edit_menu.main(self.master, self, self.text, self.menubar)
        format_menu.main(self.master, self, self.text, self.menubar)
        help_menu.main(self.master, self, self.text, self.menubar)

    def set_app_title(self, file_name):
        app_title = my_globals.BTTE_NAME() + '-'
        app_title += 'v' + my_globals.BTTE_VERSION() + '-'
        if not file_name:
            file_name = "Untitled"
        app_title += file_name
        self.master.title(app_title)


root = tk.Tk()
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

app_win = main_window(root)
app_win.build()

root.mainloop()
