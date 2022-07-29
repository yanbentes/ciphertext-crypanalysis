"""
Python3 script.

This script prints the properties of an encrypted text
aiming to help decypher the text.
"""

import print_data
# import switch
import re

with open("FILENAME", "r") as f:
    text = f.read()

# remove punctuation characters from text
alpha_text = ""
for i in text:
    if i.isalpha() is True:
        alpha_text = alpha_text + i

# calculate all the letters frequency
unique_letters = set(alpha_text)
chars_freq = dict()

for i in unique_letters:
    if i.isalpha() is True:
        chars_freq.update({i: alpha_text.count(i)})

print("Letters frequency")
# print_dict(chars_freq)
print_data.print_tuples(print_data.sort_dict(chars_freq))

# frequency of single letters
singles = re.findall(r'\b[a-z]\b', text)
unique_singles = set(singles)
singles_freq = dict()

for i in unique_singles:
    singles_freq.update({i: singles.count(i)})

print("Single letter words")
# print_dict(singles_freq)
print_data.print_tuples(print_data.sort_dict(singles_freq))

# frequency of letters at the beggining of a word
first = re.findall(r'^g|\b[a-z]', text)
unique_first = set(first)
first_freq = dict()

for i in unique_first:
    first_freq.update({i: first.count(i)})

print("First letters in a word")
# print_dict(singles_freq)
print_data.print_tuples(print_data.sort_dict(first_freq))

# frequency of letters in the end of a word
last = re.findall(r'[a-z]\b', text)
unique_last = set(last)
last_freq = dict()

for i in unique_last:
    last_freq.update({i: last.count(i)})

print("Last letters in a word")
# print_dict(singles_freq)
print_data.print_tuples(print_data.sort_dict(last_freq))

# digraphs frequency
digraphs = re.findall(r'\b[a-z][a-z]\b', text)
unique_digraphs = set(digraphs)
digraphs_freq = dict()

for i in unique_digraphs:
    digraphs_freq.update({i: digraphs.count(i)})

print("Two letters word")
# print_dict(digraphs_freq)
print_data.print_tuples(print_data.sort_dict(digraphs_freq))

# trigraphs frequency
trigraphs = re.findall(r'\b[a-z][a-z][a-z]\b', text)
unique_trigraphs = set(trigraphs)
trigraphs_freq = dict()

for i in unique_trigraphs:
    trigraphs_freq.update({i: trigraphs.count(i)})

print("Three letters word")
# print_dict(trigraphs_freq)
print_data.print_tuples(print_data.sort_dict(trigraphs_freq))

# to print the switch modifications uncomment the lines below
# for i in text:
#     if i.isalpha() is True:
#         print(switch.switch_letters(i), end="")
#     else:
#         print(i, end="")
