from common_imports import *
from tkFileDialog import *
from tkMessageBox import *
import file_menu
import edit_menu
root = Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

file_menu.main(root,text)
edit_menu.main(root,text)

root.mainloop()