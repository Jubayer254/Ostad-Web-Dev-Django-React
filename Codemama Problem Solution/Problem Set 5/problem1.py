# Rectangle in Circle

# Problem Statement
# Write a program to create a function that takes three numbers — the width and height of a rectangle, and the radius of a circle — and returns true if the rectangle can fit inside the circle, false if it can't.

# Input
# The input consists of three double numbers: width, height, radius

# Output
# The output will print either "true" or "false"

# Constraints
# 0 ≤ |S| ≤ 104
# Example:
# Enter numbers

# Input:
# 8 6 5
# Output:
# true

import math
def is_fit():
    s =  input()
    parts = s.split()
    width_r, height_r, radius_c = float(parts[0]), float(parts[1]), float(parts[2])
    diagonal_r = math.sqrt(math.pow(width_r, 2) + math.pow(height_r, 2))
    diameter_c  = 2 * radius_c

    if diagonal_r > diameter_c:
        return "false"
    else:
        return "true"

print(is_fit())