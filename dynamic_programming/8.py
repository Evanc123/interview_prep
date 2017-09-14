""" Given an infinite number of quarters, dimes, nickels and pennies, write 
code to calculate the number of ways of represeneting n cents"""



n = 26

coins = [1, 5, 10, 25]

a = {0:1}


for i in range(1, n):
    a[i] = 0
    for c in coins:
        count = 0
        tmp = i
        while (tmp - c >= 0):
            count += 1
            tmp = tmp - c
        a[i] += count

        # if a.has_key(i - c):
        #     a[i] += a[i - c]

print a