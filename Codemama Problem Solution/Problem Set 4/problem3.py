# Kinetic Energy

# Problem Statement
# Write a program that will calculate Kinetic Energy. It can be calculated with the following formula: KE = 0.5mV*V where m is mass in kg, v is velocity in m/s, KE is kinetic energy in J. Return the Kinetic Energy in Joules, given the mass and velocity. For the purposes of this challenge, round answers to the nearest integer.

# Input
# The input consists of two double number: mass and velocity.

# Output
# The output will print an integer.

# Constraints
# 0 ≤ |S| ≤ 104
# Example:
# Enter numbers

# Input:
# 60 3
# Output:
# 270

def ke(m, v):
    return 0.5 * m * v * v

s = input()
parts = s.split()
print(int(ke(float(parts[0]), float(parts[1]))))