FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):           # Default parameter
    """ Read a text file and
    return the list of to do extracted from it"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a list of todos in a textfile"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":      # The current file where this statement is, is the main
    print(get_todos())