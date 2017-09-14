
"""a"""

a = [2, 4, 0, 2]  # Magic index is the last one


def magic_index(arr):

    for i in range(len(arr)):
        if a[i] == i:
            return True
    return False


print magic_index(a)


"""b) what if the values are not distinct?"""

""" Use the insight that if the array is sorted, we can use a binary tree like 
mechanism. Start in the middle, and we can prune if the median is already to large,
for example if A[5] = 4, then we knkow that the magic index must be on the right side,
as everything before 5 will be less than 4.a

In the follow up case, we can skip some elements as well.
"""

