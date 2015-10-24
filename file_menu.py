from common_imports import *
from tkFileDialog import *
from tkMessageBox import *
import sys
class File():
	
	def newFile(self):
		self.filename = "Untitled"
		self.text.delete(0.0, END)
	
	def saveFile(self):
		try:
			t = self.text.get(0.0, END)
			f = open(self.filename, 'w')
			f.write(t)
			f.close()
		except:
			self.saveAs()
	
	def saveAs(self):
		f = asksaveasfile(mode='w', defaultextension='.txt')
		t = self.text.get(0.0, END)
		try:
			f.write(t.rstrip())
		except:
			showerror(title="Oops!", message="Unable to save file...")
	
	def openFile(self):
		f = askopenfile(mode='r')
		self.filename = f.name
		t = f.read()
		self.text.delete(0.0, END)
		self.text.insert(0.0, t)
		
	def __init__(self,text):
		self.filename = None
		self.text = text

def main(root,text):
	menubar = Menu(root)
	filemenu = Menu(menubar)
	objFile = File(text)
	filemenu.add_command(label="New", command=objFile.newFile)
	filemenu.add_command(label="Open", command=objFile.openFile)
	filemenu.add_command(label="Save", command=objFile.saveFile)
	filemenu.add_command(label="Save As...", command=objFile.saveAs)
	filemenu.add_separator()
	filemenu.add_command(label="Quit", command=root.quit)
	menubar.add_cascade(label="File", menu=filemenu)
	root.config(menu=menubar)
	
if __name__ == "__main__":
	print ("Please run 'main.py'")		