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
import tkinter.simpledialog as tksimpledialog
# from tkinter.filedialog import *
# from tkinter.messagebox import *


class Edit():

    def popup(self, event):
        self.rightClick.post(event.x_root, event.y_root)

    def copy(self, *args):
        sel = self.text.selection_get()
        self.clipboard = sel

    def cut(self, *args):
        sel = self.text.selection_get()
        self.clipboard = sel
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def paste(self, *args):
        self.text.insert(tk.INSERT, self.clipboard)

    def selectAll(self, *args):
        self.text.tag_add(tk.SEL, "1.0", tk.END)
        self.text.mark_set(0.0, tk.END)
        self.text.see(tk.INSERT)

    def undo(self, *args):
        self.text.edit_undo()

    def redo(self, *args):
        self.text.edit_redo()

    def find(self, *args):
        self.text.tag_remove('found', '1.0', tk.END)
        target = tksimpledialog.askstring('Find', 'Search String:')
        if target:
            idx = '1.0'
            while 1:
                idx = self.text.search(target, idx, nocase=1, stopindex=tk.END)
                if not idx:
                    break
                lastidx = '%s+%dc' % (idx, len(target))
                self.text.tag_add('found', idx, lastidx)
                idx = lastidx
            self.text.tag_config('found',
                                 foreground='white',
                                 background='blue')

    def __init__(self, text, root):
        self.clipboard = None
        self.text = text
        self.rightClick = tk.Menu(root)


def main(root, main_win, text, menubar):
    objEdit = Edit(text, root)
    editmenu = tk.Menu(menubar)
    editmenu.add_command(label="Copy",
                         command=objEdit.copy,
                         accelerator="Ctrl+C")
    editmenu.add_command(label="Cut",
                         command=objEdit.cut,
                         accelerator="Ctrl+X")
    editmenu.add_command(label="Paste",
                         command=objEdit.paste,
                         accelerator="Ctrl+V")
    editmenu.add_command(label="Undo",
                         command=objEdit.undo,
                         accelerator="Ctrl+Z")
    editmenu.add_command(label="Redo",
                         command=objEdit.redo,
                         accelerator="Ctrl+Y")
    editmenu.add_command(label="Find",
                         command=objEdit.find,
                         accelerator="Ctrl+F")
    editmenu.add_separator()
    editmenu.add_command(label="Select All",
                         command=objEdit.selectAll,
                         accelerator="Ctrl+A")
    menubar.add_cascade(label="Edit", menu=editmenu)

    root.bind_all("<Control-z>", objEdit.undo)
    root.bind_all("<Control-y>", objEdit.redo)
    root.bind_all("<Control-f>", objEdit.find)
    root.bind_all("Control-a", objEdit.selectAll)

    objEdit.rightClick.add_command(label="Copy", command=objEdit.copy)
    objEdit.rightClick.add_command(label="Cut", command=objEdit.cut)
    objEdit.rightClick.add_command(label="Paste", command=objEdit.paste)
    objEdit.rightClick.add_separator()
    objEdit.rightClick.add_command(label="Select All",
                                   command=objEdit.selectAll)
    objEdit.rightClick.bind("<Control-q>", objEdit.selectAll)

    text.bind("<Button-3>", objEdit.popup)

    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'main.py'")
