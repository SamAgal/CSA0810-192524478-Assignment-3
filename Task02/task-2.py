"""Task 2: Tuples, Mutability and Copying (City Bus-Stop Map)."""

import sys

if __name__ == "__main__":
    rows, cols = 3, 4
    
    # Buggy grid creation
    bad = [[0] * cols] * rows
    bad[0][1] = 7
    
    # Corrected grid using list comprehension
    good = [[0 for _ in range(cols)] for _ in range(rows)]
    good[0][1] = 7
    
    print("bad :", bad)
    print("good:", good)
    print("bad[0] is bad[1]:", bad[0] is bad[1])
    print("good[0] is good[1]:", good[0] is good[1])
    
    # Tuples as dictionary keys
    stops = {(13.0827, 80.2707): "Chennai Central", (13.0418, 80.2341): "T. Nagar"}
    print("Stop lookup:", stops[(13.0418, 80.2341)])
    
    try:
        d = {[13.0418, 80.2341]: "Invalid"}
    except TypeError as e:
        print("List as dict key error caught:", type(e).__name__)
