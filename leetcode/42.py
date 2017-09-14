"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""


a = [0,1,0,2,1,0,1,3,2,1,2,1]


def water_height(arr):
    max_height = 0
    water_count = 0
    for i in range(len(arr)):
        if a[i] > max_height:
            a[i] = max_height