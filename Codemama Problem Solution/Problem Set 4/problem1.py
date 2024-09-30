# Gamble with Profit

# Problem Statement
# Write a program that takes three arguments prob, prize, pay and returns true if prob * prize > pay; otherwise return false.

# Input
# The input consists of one float F F and two integer N N, M M numbers

# Output
# The output will print either "true" or "false"

# Constraints
# 0 ≤ |F| ≤ 1
# 0 ≤ |N| ≤ 104
# 0 ≤ |M| ≤ 104
# Example:
# Enter numbers

# Input:
# 0.2 50 9
# Output:
# true

def func(prob, prize, pay):
    if prob * prize > pay:
        return "true"
    return "false"

s = input()
parts = s.split()
print(func(float(parts[0]), int(parts[1]), int(parts[2])))