# Exception Handling in Python
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