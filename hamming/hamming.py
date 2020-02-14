##
## EPITECH PROJECT, 2019
## hamming
## File description:
## hamming.py
##

def distance(strand_a, strand_b):
    diff = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Two strands aren't the same lenght.")
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            diff += 1
    return (diff)
    
