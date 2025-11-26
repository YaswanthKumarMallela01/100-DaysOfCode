piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

'''Slicing in Python is a powerful and flexible way to extract specific portions 
(subsequences) from sequential data types like lists, strings, and tuples'''

print(piano_keys[2:5])  # Prints content from index 2 to 5
print(piano_keys[2:])  # Prints content from index 2 to the end of the list
print(piano_keys[:5])  # Prints content from index starting(0th index) to 5
print(piano_keys[2:5:2])  # Prints content from index 2 to 5 with the step of 2
print(piano_keys[::2])  # Prints content from index 0 to end of the list but with step 2
print(piano_keys[::-1])  # Reverses the List
