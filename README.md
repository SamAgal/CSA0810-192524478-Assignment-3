# CSA08 - Python Programming: Assignment 3
**Title:** Data Structures: Lists, Tuples, Dictionaries, Sets, and Comprehensions Laboratory  
**Name:** J. Sam Agal  
**Register Number:** 192524478  
**Course:** CSA08 - Python Programming (CO3 Coverage)  
**Python Version:** Python 3.12  
**Libraries Used:** Python Standard Library only (`time`, `random`, `copy`, `collections`, `sys`) — see `requirements.txt`

## Commands Used to Run Each Program
Run all programs from the root directory of the repository:
```bash
python Task01/task-1.py
python Task02/task-2.py
python Task03/task-3.py
python Task04/task-4.py
python Task05/task-5.py
python Task06/task-6.py
python Task07/task-7.py
```

## Summary of Task Results
- **Task 01 (Lists & Slicing):** Analysed 365 daily rainfall records using slicing (`readings[7:14]`, `readings[-7:]`, `readings[::7]`), computed weekly totals, wettest/driest periods, and compared naive moving average ($O(n \cdot k)$) vs running sum ($O(n)$).
- **Task 02 (Tuples, Mutability & Copying):** Modelled GPS coordinate pairs as dictionary keys, fixed the nested list multi-row aliasing bug (`[[0]*cols]*rows`) using list comprehensions, and demonstrated shallow vs deep copies.
- **Task 03 (Dictionaries):** Analysed Kisan Helpline complaints using dictionary frequency counts, `get()` / `setdefault()`, `collections.Counter`, and stop-word filtering.
- **Task 04 (Sets):** Detected elective registration clashes using set operators (`&`, `-`, `^`, `|`) vs nested loops, proving $O(1)$ set lookups.
- **Task 05 (List Comprehensions):** Cleaned vaccine cold-storage temperature sensor readings comparing `for` loops, list comprehensions with conditions, and `map()`/`filter()` with `lambda`.
- **Task 06 (Nested Data):** Processed a railway timetable using nested dictionaries, lists, and sorting algorithms.
- **Task 07 (Contact Merging):** Designed a robust contact-merging program from first principles, merging records based on overlapping phone numbers and emails using union-find/connected components.
