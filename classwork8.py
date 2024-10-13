"""

import logging


logging.basicConfig(level=logging.DEBUG, filename="error.log", format="%(asctime)s - %(levelname)s - %(message)s")

def devide(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError as e:
        logging.info(f"Division by zero error: {e}")

devide(10,0)

"""

"""
>>> 2+2
4
"""
if __name__== "__main__":
   import doctest
   doctest.testmod()

