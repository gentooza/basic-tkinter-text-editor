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


class mainWindow:

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
        self.selectedText = None
        '''configure events'''
        self.events()

    def build(self):
        self.fileMenu = file_menu.fileMenu(self.text, self.master, self)
        self.editMenu = edit_menu.editMenu(self.text, self.master, self)
        format_menu.main(self.master, self, self.text)
        help_menu.main(self.master, self, self.text)

    def events(self):
        self.text.bind("<<Selection>>", self.ev_selected_text)

    def set_app_title(self, file_name):
        app_title = my_globals.BTTE_NAME() + '-'
        app_title += 'v' + my_globals.BTTE_VERSION() + '-'
        if not file_name:
            file_name = "Untitled"
        app_title += file_name
        self.master.title(app_title)

    '''EVENTS'''
    def ev_selected_text(self, event):
        oldSelectedText = self.selectedText
        try:
            self.selectedText = self.text.get(tk.SEL_FIRST, tk.SEL_LAST)
        except:
            self.selectedText = None
        ''' update edit menu'''
        if oldSelectedText != self.selectedText:
            self.edit_menu.update()


root = tk.Tk()
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

appWin = mainWindow(root)
appWin.build()

root.mainloop()
