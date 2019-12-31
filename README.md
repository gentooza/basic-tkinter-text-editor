# tkinter-text-editor
Fork of https://github.com/punithpatil/tkinter-text-editor

Simple text editor designed in Python 3 using the Tkinter library.

Pep8 compliance, we are going to fix old bugs, correct source code licensing, some improvements also. It's going to be useful for reusing it in bigger projects based in GUI text edition.

# Library required
For Python 3.0 and above

`sudo apt install python3-tk`

# Bugs
Format menu
-----------
+ Changing font type and font size is non functional.
+ Font styles (Bold, Italic, Underline, Overstrike) are only applicable if text is already selected.

Edit menu
---------
+ Cut, copy, paste are not synced when selected from editmenu/rightclick and keyboard shortcuts(*i.e.* both may store different instances, and hence output different values)

# Improvements
Format menu
----------
+ can turn on/off by configuration possibility of change font type, size and styles (in some projects, we don't need this tools)