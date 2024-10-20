# Longest Substring Without Repeating Character

# Problem Statement
# Write a program to find the length of the longest substring in a given string without repeating characters. For example, in the string "abcabcbb," the longest substring without repeating characters is "abc," which has a length of 3.

# Input
# The program will take a string as input.

# Output
# The output will be the length of the longest substring which will be an integer.

# Constraints
# 0 ≤ |S| ≤ 1000
# Example:
# Enter string

# Input:
# abcabcbb
# Output:
# 3


def length_of_longest_substring(s):
    seen_chars = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in seen_chars:
            start = max(start, seen_chars[s[end]] + 1)

        seen_chars[s[end]] = end

        max_length = max(max_length, end - start + 1)

    return max_length

s = input()
print(length_of_longest_substring(s))
