"""List comprehension in Python offers a concise and efficient way to create new lists
based on existing iterables (like lists, tuples, or strings). It combines looping and
conditional logic within a single line, often making code more readable and sometimes faster
than traditional for loops."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_numbers = [n * n for n in numbers]
print(square_numbers)

name = "yaswanth"
name_chars = [letter for letter in name]
print(name_chars)

cube_numbers = [n * n * n for n in range(1, 11)]
print(cube_numbers)

names = ["Rama", "Sita", "Lakshmana", "Ravana"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
large_names = [name.upper() for name in names if len(name) > 5]
print(large_names)
