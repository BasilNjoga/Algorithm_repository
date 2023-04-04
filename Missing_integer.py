#!/usr/bin/python3

# you can write to stdout for debugging purposes, e.g.
print("this is a debug message")
"""
It searches for the smallest possible missing integer from 1 to 100, 0000
"""


newlist = []
A = [-1, -3, -6, 15, 4, 2]
mynum = 0
value = True

def solution(A):
    for i in range(len(A)):
        for j in range(len(A) - 1):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
    print(A)
    value = True
    for m in range(1,10):
        if(value == True):
            for k in range(len(A)):
                if m == A[k]:
                    value = True
                    print(f"{m} is finished")
                    break
                else:
                    value = False
        else:
            return(m - 1)

print(solution(A))

