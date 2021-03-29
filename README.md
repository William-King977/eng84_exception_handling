# File and Exception Handling in Python
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