""" Write a method to compute all permutations of a string"""


def permutations(val):
    
    if len(val) == 1:
        return val

    for i in range(len(val)):
        chosen_char = val[i]
        permutations(val[:i] + val[i+1:])




a = 'string'


print a[1:]
