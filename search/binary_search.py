


def binary_search_recur(arr, target):
    """Returns True if target is in sorted arr, False otherwise""" 

    if len(arr) == 0:
        return False

    mid_point = len(arr) / 2
    
    if target == arr[mid_point]:
        return True
    elif target > mid_point:
        return binary_search_recur(arr[mid_point:], target)
    else:
        return binary_search_recur(arr[:mid_point], target)


def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif value < arr[mid]:
            hi = mid - 1
        else:
            return mid
    return None






a = [1, 2, 3, 4, 6, 8, 9, 10]

print binary_search_recur(a, 4)