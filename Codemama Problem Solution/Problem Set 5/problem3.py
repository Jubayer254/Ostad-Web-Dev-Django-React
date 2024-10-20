# Find the Odd Integer

# Problem Statement
# Write a program to create a function that takes an array and finds the integer which appears an odd number of times.

# Input
# The program will take input until encounters a new line.

# Output
# The output will be an integer.

# Constraints
# 0 ≤ |S| ≤ 104
# Example:
# Enter numbers

# Input:
# 1 1 2 -2 5 2 4 4 -1 -2 5
# Output:
# -1 

from collections import Counter

def odd_counter():
    s =  input()
    parts = s.split()
    result = Counter(parts)

    odd = -1
    for element, count in result.items():
        if count%2 != 0:
            odd = element

    return odd

print(odd_counter())