"""Write a method to return all subsets of a set"""




def get_subsets(arr, idx):
    """takes O(2^n)"""
    all_subsets = [[]]
    if len(arr) == idx:
        pass
    else:
        all_subsets = get_subsets(arr, idx + 1)
        item = arr[idx]
        more_subsets = []
        for subset in all_subsets:
            new_subset = []
            new_subset.append(subset)
            new_subset.append(item)
            more_subsets.append(new_subset)
        all_subsets.append(more_subsets)
    return all_subsets

a = ['a', 'b', 'c']


print get_subsets(a, 0)


""" Even cleverer, generate all binary numbers from 0 to 2^n, and map them to an array"""