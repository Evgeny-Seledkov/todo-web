FILEPATH = "/Users/evgenyseledkov/PycharmProjects/WebApp1/pythonProject/todos.txt"


def get_todos(filepath=FILEPATH):  # default parameter setting up
    """ Read a text file and return the list
    of to-do items.
    """
    with open(filepath, 'r') as file_local:  # better way to handle files. No need to close file manually
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):  # two parameters, but only one has default value - order matters
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

# print(__name__) - return __main__ if it's executed from the current module
# and name of the module if it's executed outside


if __name__ == "__main__":  # construction to execute following code only in functions module
    print("Hello")
    print(get_todos())