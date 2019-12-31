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
import tkinter.filedialog as tkfiledialog
import tkinter.messagebox as tkmessagebox
import sys


class File():

    def newFile(self):
        self.filename = "Untitled"
        self.text.delete(0.0, tk.END)

    def saveFile(self):
        try:
            t = self.text.get(0.0, tk.END)
            f = open(self.filename, 'w')
            f.write(t)
            f.close()
        except:
            self.saveAs()

    def saveAs(self):
        f = tkfiledialog.asksaveasfile(mode='w', defaultextension='.txt')
        t = self.text.get(0.0, tk.END)
        try:
            f.write(t.rstrip())
        except:
            tkmessagebox.showerror(title="Oops!",
                                   message="Unable to save file...")

    def openFile(self):
        f = tkfiledialog.askopenfile(mode='r')
        self.filename = f.name
        t = f.read()
        self.text.delete(0.0, tk.END)
        self.text.insert(0.0, t)
        # TODO: it should be a function
        app_title = my_globals.BTTE_NAME() + '-'
        app_title += 'v' + my_globals.BTTE_VERSION() + '-'
        app_title += f.name
        self.root.title(app_title)
        # 

    def quit(self):
        entry = tkmessagebox.askyesno(title="Quit",
                                      message="Are you sure you want to quit?")
        if entry is True:
            self.root.destroy()

    def __init__(self, text, root):
        self.filename = None
        self.text = text
        self.root = root


def main(root, text, menubar):
    filemenu = tk.Menu(menubar)
    objFile = File(text, root)
    filemenu.add_command(label="New",
                         command=objFile.newFile)
    filemenu.add_command(label="Open",
                         command=objFile.openFile)
    filemenu.add_command(label="Save",
                         command=objFile.saveFile)
    filemenu.add_command(label="Save As...",
                         command=objFile.saveAs)
    filemenu.add_separator()
    filemenu.add_command(label="Quit",
                         command=objFile.quit)
    menubar.add_cascade(label="File",
                        menu=filemenu)
    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'main.py'")
