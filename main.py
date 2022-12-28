"""
Python3 script.

This script prints the properties of an encrypted text
aiming to help decypher the text.
"""

import print_data
import re


def switch_letters(string):
    """Do a switch statement."""
    switch = {
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
    }

    return switch.get(string, "empty")


file = str(input("Filename: "))

with open(file, "r") as f:
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
print_data.print_tuples(print_data.sort_dict(chars_freq))

# frequency of single letters
singles = re.findall(r'\b[a-z]\b', text)
unique_singles = set(singles)
singles_freq = dict()

for i in unique_singles:
    singles_freq.update({i: singles.count(i)})

print("Single letter words")
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
print_data.print_tuples(print_data.sort_dict(last_freq))

# two letters word frequency
two_letters = re.findall(r'\b[a-z][a-z]\b', text)
unique_twos = set(two_letters)
two_letters_freq = dict()

for i in unique_twos:
    two_letters_freq.update({i: two_letters.count(i)})

print("Two letters word")
print_data.print_tuples(print_data.sort_dict(two_letters_freq))

# three letter words frequency
three_letters = re.findall(r'\b[a-z][a-z][a-z]\b', text)
unique_threes = set(three_letters)
three_letters_freq = dict()

for i in unique_threes:
    three_letters_freq.update({i: three_letters.count(i)})

print("Three letters word")
print_data.print_tuples(print_data.sort_dict(three_letters_freq))

# print switch modifications
print("Text: ")
for i in text:
    if i.isalpha() is True:
        print(switch_letters(i), end="")
    else:
        print(i, end="")
