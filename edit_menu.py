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

    def build_edit_menu(self):
        self.editmenu.add_command(label="Copy",
                                  command=self.ev_copy,
                                  accelerator="Ctrl+C")
        self.editmenu.add_command(label="Cut",
                                  command=self.ev_cut,
                                  accelerator="Ctrl+X")
        self.editmenu.add_command(label="Paste",
                                  command=self.ev_paste,
                                  accelerator="Ctrl+V")
        self.editmenu.add_command(label="Undo",
                                  command=self.ev_undo,
                                  accelerator="Ctrl+Z")
        self.editmenu.add_command(label="Redo",
                                  command=self.ev_redo,
                                  accelerator="Ctrl+Y")
        self.editmenu.add_command(label="Find",
                                  command=self.ev_find,
                                  accelerator="Ctrl+F")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Select All",
                                  command=self.ev_selectAll,
                                  accelerator="Ctrl+A")
        self.main_win.menubar.add_cascade(label="Edit", menu=self.editmenu)

    def ev_popup(self, event):
        self.rightClick.post(event.x_root, event.y_root)

    def ev_copy(self, *args):
        sel = self.text.selection_get()
        self.clipboard = sel

    def ev_cut(self, *args):
        sel = self.text.selection_get()
        self.clipboard = sel
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def ev_paste(self, *args):
        self.text.insert(tk.INSERT, self.clipboard)

    def ev_selectAll(self, *args):
        self.text.tag_add(tk.SEL, "1.0", tk.END)
        self.text.mark_set(0.0, tk.END)
        self.text.see(tk.INSERT)

    def ev_undo(self, *args):
        self.text.edit_undo()

    def ev_redo(self, *args):
        self.text.edit_redo()

    def ev_find(self, *args):
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

    def update(self):
        if ((not self.main_win.selected_text)
                or (self.main_win.selected_text == '')):
            self.editmenu.entryconfig("Copy", state="disabled")
            self.editmenu.entryconfig("Cut", state="disabled")
            self.rightClick.entryconfig(1, state="disabled")
            self.rightClick.entryconfig(2, state="disabled")
        else:
            self.editmenu.entryconfig("Copy", state="normal")
            self.editmenu.entryconfig("Cut", state="normal")
            self.rightClick.entryconfig(1, state="normal")
            self.rightClick.entryconfig(2, state="normal")

    def __init__(self, text, root, main_win):
        self.clipboard = None
        self.text = text
        self.main_win = main_win
        self.rightClick = tk.Menu(root)
        self.editmenu = tk.Menu(main_win.menubar)
        self.build_edit_menu()

        root.bind_all("<Control-z>", self.ev_undo)
        root.bind_all("<Control-y>", self.ev_redo)
        root.bind_all("<Control-f>", self.ev_find)
        root.bind_all("Control-a", self.ev_selectAll)

        self.rightClick.add_command(label="Copy", command=self.ev_copy)
        self.rightClick.add_command(label="Cut", command=self.ev_cut)
        self.rightClick.add_command(label="Paste", command=self.ev_paste)
        self.rightClick.add_separator()
        self.rightClick.add_command(label="Select All",
                                    command=self.ev_selectAll)
        self.rightClick.bind("<Control-q>", self.ev_selectAll)

        self.text.bind("<Button-3>", self.ev_popup)

        root.config(menu=main_win.menubar)

        self.update()


def main(root, main_win, text):
    objEdit = Edit(text, root, main_win)

    return objEdit

if __name__ == "__main__":
    print("Please run 'main.py'")
