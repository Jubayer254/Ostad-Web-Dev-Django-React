# Consecutive Numbers

# Problem Statement
# Write a program to create a function that determines whether elements in an array can be re-arranged to form a consecutive list of numbers where each number appears exactly once. The difference between two numbers will be 1 always.

# Input
# The program will take an integer N.
# N as the size of an array. Then it will take the integer values of the array M[].

# Output
# The output will print either "true" or "false"

# Constraints
# 0 ≤ |N| ≤ 100000
# 0 ≤ |M[]| ≤ 100000
# Example-1:
# Enter numbers

# Input:
# 5
# 4 2 3 1 0
# Output:
# true
# Example-2:
# Enter numbers

# Input:
# 6
# 1 2 3 4 4 5
# Output:
# false
# Notes:
# If there are any duplicates, it's impossible to form a consecutive list

def Consecutive_Numbers(l, s):
    parts = sorted([int(part) for part in s.split()], reverse=True)
    for x in range(0, l - 1):
        r = parts[x] - parts[x+1]
        if r != 1:
            return "false"
        
    return "true"

    
l = int(input())
s =  input()
print(Consecutive_Numbers(l, s))