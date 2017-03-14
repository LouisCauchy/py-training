# quadratic

import math
import cmath
import sys

def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("Zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x
