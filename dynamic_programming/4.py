"""Write a method to return all subsets of a set"""




def subset_recur(arr, power_set):
    if len(arr) == 0:
        import pdb; pdb.set_trace()
        return []
    # import pdb; pdb.set_trace()
    for i in range(len(arr)):

        subset = subset_recur(arr[:i] + arr[i + 1:], power_set)
        if not(subset in power_set):
            power_set.append(arr)
    return power_set


a = ['a', 'b', 'c']


print subset_recur(a, [])


""" Even cleverer, generate all binary numbers from 0 to 2^n, and map them to an array"""