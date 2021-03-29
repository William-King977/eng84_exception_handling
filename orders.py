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
        file = open(file_name, "r")
        print("Contents of the file:")
        print(file.read())
        file.close()
    except FileNotFoundError as err:
        print(f"The file named '{file_name}' does not exist - {err}.")


# Forth iteration
# Write an item to the file
def write_to_file(file_name, item):
    try:
        file = open(file_name, "a")
        file.write(item + "\n") # also adds a new line
        file.close()
        print(f"{item} written into {file_name} successfully.")
    except FileNotFoundError as err:
        print(f"The file named '{file_name}' does not exist - {err}.")


# main program
print("Reading files:")
read_file("orders.txt")
read_file("wsm_winners.txt")

# Adding a new item
print("Adding a new item: ")
write_to_file("orders.txt", "ice cream")
read_file("orders.txt")