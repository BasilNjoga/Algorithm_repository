#!/usr/bin/python3
"""
This is an insertion sort, not the best for large arrays but for smaller it's easy
to implement and works
works for even negative numbers
changing the sign in the if statement shifts the order
"""

arr = [1,4, 5, 7, 9 , 40]
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr)