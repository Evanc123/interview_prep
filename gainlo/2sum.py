"""
given a sorted array, find 2 numbers that sum up to S.
"""

def twoSum(arr, target):
    dict = {}

    # for all elements in the array
    for i in range(len(arr)):
        # set the complment as the searched for as the target
        # minus the current value.
        complement = target - arr[i]
        # we are now searching for if the current complement is in the list.
        # this works in the first case because:
        # dict[0] = 9 - 2 = 7, and dict[1] = 9 - 7 = 2
        if complement in dict:
            return True
        dict[arr[i]] = i

    return False

# Test
print twoSum([2, 7, 11, 15], 9) # True
print twoSum([2, 7, 11, 15], 3) # False



"""
Another way to do this: 

To solve this in O(N) time, we can keep two indices – one in the beginning (start) and the other in the end (end). If the sum of the current two numbers is greater than S, we move the end pointer backward by one step. If the sum is smaller than S, we move the start pointer forward by one step.

When the two pointers meet each other, we know that no two numbers sum up to S. The reason we can make it O(N) is that the array is sorted and we don’t need to check all the combinations.


"""