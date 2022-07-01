"""

Purpose: This program extracts SSN data from a text file. They are outputted in the order
         they appear in the data. Format of the SSN is XXX-XX-XXXX

"""
import re

# Opening and reading the file
input_file = open("regexData2.txt", 'r')

# Creating the search pattern
pattern = "(\d{3}) [- ]?(\d{2}) [- ]?(\d{4})"


# Outputting the numbers using the regex pattern / reading the data file
print("Social Security Numbers:")
print(list(map("-".join, (re.findall(pattern, input_file.read())))))




input_file.close()

