"""

File: regex_machine1.py
Purpose: This program uses regex to find the number of times
         any instance of the word 'python' (case insensitive) appears in the source.

"""
import re

# Opening the file to read
input_file = open("regexData1.txt", 'r')
file = input_file.read()

# Creating pattern to scan the file with
pattern = "(?i)python"

# Counting instances of the word "python" in the file
matches = len(re.findall(pattern, file))


# Output the results
print("Occurences of Python in the file:", matches)


# closing the file
input_file.close()
