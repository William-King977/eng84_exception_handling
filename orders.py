# Dealing with files and error/exception handling

# open() is used find a file.
# file = open("orders.txt") # FileNotFoundError

try:
    file = open("orders.txt")
    print("File was found.")
except FileNotFoundError as err:
    print(f"The above block of code was not executed - {err}.")
    # raise
finally:
    print("Your task is to read the data and display it as a list.")

# Second iteration:
# Your task is to read the data and display it as a list.

# Third
