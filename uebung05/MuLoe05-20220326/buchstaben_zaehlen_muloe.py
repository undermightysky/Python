# -*- coding: utf-8 -*-

from pathlib import Path
from string import ascii_lowercase

# Read the entire text file and make all lower case.
text = Path('zen.txt').read_text(encoding='utf-8').lower()

# Alternative solution without pathlib:
# with open('zen.txt', encoding='utf-8') as file:
#     text = file.read()

# Count the occurrence of the alphabetic characters in the text.
chars = {c: text.count(c) for c in ascii_lowercase}

# Create a sorted list of the alphabetic characters, by descending occurrence.
# chars_sorted = sorted(chars.keys(), key=lambda x: chars[x], reverse=True)
chars_sorted = sorted(chars.keys(), key=chars.get, reverse=True)

print(chars)
print(chars_sorted)
