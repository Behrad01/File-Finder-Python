# File-Finder-Python

I made this script to speed up the process of finding files since the built-in method of file searching on Windows is super slow. This one works under 10 seconds and gives the result, though the time might change depending on the amount of files you have but on average it's under 10 seconds.

### Note
This script currently works on Windows only (uses drive letters like C:\, D:\). For Linux/Mac, it would need modification.

## Features

- Searches all drives on your Windows computer (C:\, D:\, etc.)
- Finds both **files** and **folders**
- Case-insensitive search (finds "Document", "document", and "DOCUMENT")
- Shows full paths in a numbered list
- Clears the terminal before each search for a clean interface
- Handles drives that don't exist (skips them automatically)
- Tells you if no matching paths are found

## Example
Input: "documents"
Output: 
1. C:\Users\Behrad\Documents\resume.docx
2. C:\Users\Behrad\Desktop\important_document.pdf
3. C:\Users\Behrad\Downloads\document.txt
4. C:\Users\Behrad\Pictures\scanned_document.jpg

The script also tells you if no path is found, keep in mind it takes a few seconds after input for the paths to appear in the terminal
