""" Given an infinite number of quarters, dimes, nickels and pennies, write 
code to calculate the number of ways of represeneting n cents"""

coins = [1, 5, 10, 25]



def make_change(n, start_coin):
    """Computes the number of ways to write n cents"""
    next_denom = 0
    
    if start_coin == 25:
        next_denom = 10
    elif start_coin == 10:
        next_denom = 5
    elif start_coin == 5:
        next_denom = 1
    else:
        return 1
    ways = 0
    for i in range(0, n + 1, start_coin):
        ways += make_change(n - i * start_coin, next_denom)

    return ways

print make_change(99, 25)
