# Basic Tkinter Text Editor
Fork of https://github.com/punithpatil/tkinter-text-editor

Basic Simple Text Editor designed in Python 3 using the Tkinter library.

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

# Copyright

Copyright (C) 2015 Punith Patil <br/>
Copyright (C) 2019-2020 Joaquín Cuéllar

# License

```
Basic Simple Text Editor is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Basic Simple Text Editor is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```