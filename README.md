# CodeReader
This repo reads a file and returns the total no. of blank lines, comments and executable lines in a file.

# Assumptions:
- The language it is reading right now is Python
- The file to read is uploaded in the root directory.
- Like in Python, Single Line Comments cannot be closed. (So no piece of code can be written after an inline comment)
- Multiline comments are not allowed.
- There are no invalid inputs. E-g-
    - A line in the file will always be either comment, code or Blank.

# How to run
1. Clone this repo.
2. Install Python3.7 globally or using a virtual environment of your choice.
3. To run, use `python index.py` command.

Note: Depending on the installation, you may have to user `python3` instead of `python`
