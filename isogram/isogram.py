##
## EPITECH PROJECT, 2019
## isogram
## File description:
## isogram.py
##

def is_isogram(string: str):
    string = string.lower().replace(' ', '').replace('-', '')
    return len(string) == len(set(string))