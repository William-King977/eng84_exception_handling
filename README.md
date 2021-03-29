# File and Exception Handling in Python
## Exception handling
We have `try`, `except`, `raise` and
`finally` as our code blocks to handle the
errors or exceptions.

To understand the concept easily:
 * Each block of code works as an `if`,
   `elif`, `else` block
   
An example of handling an exception. Add an `orders.txt` file
to prevent an exception from being raised.
```python
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
```

## File handling
### File handling modes
| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|

### File reading
The contents of a file can be read by doing the following:
```python
# Prints line by line
def read_file(file_name):
    try:
        file = open(file_name, "r")
        print("Contents of the file:")
        print(file.read())
        file.close()
    except FileNotFoundError as err:
        print(f"The file named '{file_name}' does not exist - {err}.")

read_file("orders.txt")
```

### File writing
The following code writes a string into a file. The example
also adds a new line.
````python
def write_to_file(file_name, item):
    try:
        file = open(file_name, "a")
        file.write(item + "\n") # also adds a new line
        file.close()
        print(f"{item} written into {file_name} successfully.")
    except FileNotFoundError as err:
        print(f"The file named '{file_name}' does not exist - {err}.")

write_to_file("orders.txt", "ice cream")
````