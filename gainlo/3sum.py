'''
Determine if any 3 integers in an array sum to 0.

For example, for array [4, 3, -1, 2, -2, 10], the function 
should return true since 3 + (-1) + (-2) = 0. To make things simple,
each number can be used at most once.
'''

'''
1. Naive Solution is to test every 3 numbers to test if it is zero
2. is it possible to cache sum every two numberse, then see if the rest make zero?

Insight: we need enough "power" in the negative numbers to reduce the positive numbers. 
Count up the negative numbers summed to see the maximum negative number. 

Possibly create some sort of binary search tree, where all the sums are the roots? No 
that wouldn't work. 
'''

def sum_2(arr, target):
    dict = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in dict:
            return True
        dict[arr[i]] = i
    return False

def sum_3(arr):
    arr.sort() 
    for i in range(len(arr)):
        if sum_2(arr[:i] + arr[i+1:], -arr[i]):
            return True
    return False


test =  [4, 3, -1, 2, -2, 10]
assert sum_3(test) == True

test = [4, -4, 0]
assert sum_3(test) == True

test = [4, -3, -1]
assert sum_3(test) == True

test = [0, 0, 1]
assert sum_3(test) == False

test = [0, 2, -1, -5, 20, 10, -2]
assert sum_3(test) == True

