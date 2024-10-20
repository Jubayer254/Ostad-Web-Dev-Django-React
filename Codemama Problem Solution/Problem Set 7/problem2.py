# First Occurrence Finding

# Problem Statement
# Write a program where you will be given a sorted array of integers and a target value.There will be repeated elements. Find the index of the first occurrence of the target in the array using binary search.

# Input
# The program will take an integer N.
# N as the size of a sorted array. Then it will take the integer values of the array M[].
# Finally, it will take the target value P.

# Output
# The output will print either the index of the first occurrence of the target element or "Element not found" if the element is not found.

# Constraints
# 0 ≤ |N| ≤ 100000
# 0 ≤ |M[]| ≤ 100000
# 0 ≤ |P| ≤ 100000
# Example-1:
# Enter numbers

# Input:
# 9
# 1 2 2 4 4 4 5 6 7
# 4
# Output:
# 3
# Example-2:
# Enter numbers

# Input:
# 9
# 1 2 2 4 4 4 5 6 7
# 8
# Output:
# Element not found
# Notes:
# None

def first_occurrence_finding(arr, low, high, x):

    while low <= high:
        index = (low + high) // 2

        if arr[index] == x:
            if index == 0 or arr[index - 1] != x:
                return index
            else:
                high = index - 1 

        elif arr[index] > x:
            high = index - 1
        else:
            low = index + 1
                
    return "Element not found"

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(first_occurrence_finding(arr, 0, n-1, x))