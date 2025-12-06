try:
    '''Trying dangerous code in try block to catch the exception which will effect the execution
    of the entire code. This will raise no error during compile time'''

    file = open("data_a.txt")  # This will raise FileNotFoundError as data_a.txt file doesn't exist
    dictionary = {'key': 'value'}
    dict_data = dictionary["something_not_in_the_dictionary"]  # This will raise KeyError as key is not present in dictionary
except FileNotFoundError:
    '''This will be implemented if FileNotFoundError occurs without crashing the code'''

    print("File named doesn't exists. Creating a new file")
    file = open("data_a.txt", "w")
    file.write("Hello! How are you")
except KeyError as key:
    '''This will be implemented if KeyError occurs without crashing the code'''

    print(f"The key {key} doesn't exist")
else:
    '''This else block will be implemented if try block succeeds'''
    data = file.read()
    print(data)
finally:
    '''This finally block will be implemented no matter what'''
    file.close()
