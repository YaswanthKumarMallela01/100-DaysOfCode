"""This is one way to open read files, as we should not forget about closing file at the end.
So there is another method to open, read, write, append and so on without need to add another
statement for closing file."""
# file = open("My_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("My_file.txt", mode="a") as file:  # r = read, w = write, a = append
    file.write("\nThis is appended from main.py")

"""We are currently in Learnings folder. So Learnings folder will be root folder"""
"""Accessing data.txt from improvement(Snake game) using absolute file path"""
#  Absolute file path: "D:\PY\100-DaysOfCode\Day024\Improvement(Snake game)\data.txt"

"""Accessing My_file.txt from Learnings using relative file path"""
#  Relative file path: ".\My_file.txt"

"""Accessing data.txt from improvement(Snake game) using relative file path"""
#  Relative file path: "..\data.txt" .
#  Add ..\ any times you want to go to previous folders. One ..\ goes to one previous folder.

