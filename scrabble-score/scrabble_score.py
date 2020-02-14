##
# EPITECH PROJECT, 2019
# scrabble-score
# File description:
# scrabble_score.py
##


def score(word: str):
    one = "AEIOULNRST"
    two = "DG"
    three = "BCMP"
    four = "FHVWY"
    five = "K"
    eight = "JX"
    ten = "QZ"
    ret = 0
    for letter in word.upper():
        if letter in one:
            ret += 1
        elif letter in two:
            ret += 2
        elif letter in three:
            ret += 3
        elif letter in four:
            ret += 4
        elif letter in five:
            ret += 5
        elif letter in eight:
            ret += 8
        elif letter in ten:
            ret += 10
    return ret
