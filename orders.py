# Dealing with files and error/exception handling

# open() is used find a file.
# file = open("orders.txt") # FileNotFoundError

# try:
#     file = open("orders.txt")
#     print("File was found.")
# except FileNotFoundError as err:
#     print(f"The above block of code was not executed - {err}.")
#     # raise
# finally:
#     print("Your task is to read the data and display it as a list.")

# Second iteration:
# Your task is to read the data and display it as a list.
# print(file.read())

# Third iteration
# Create a function to do the same job (DRY)
def read_file(file_name):
    try:
        file = open(file_name)
        print("Contents of the file:")
        print(file.read())
    except FileNotFoundError as err:
        print(f"The file named '{file_name}' does not exist - {err}.")


# main program
read_file("orders.txt")
read_file("wsm_winners.txt")