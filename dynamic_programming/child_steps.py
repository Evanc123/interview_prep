
"""
A child is running up a staircase with n steps, and can hop either 1 step, 
2 steps, or 3 steps. Implement a method to count how many possible ways the child can
run up the stairs
"""

def number_of_steps_dp(n, map):

    for i in range(1, n + 1):
        map[i] = 0
        if map.has_key(i - 1):
            map[i] += map[i - 1]
        if map.has_key(i - 2):
            map[i] += map[i - 2]
        if map.has_key(i - 3):
            map[i] += map[i - 3]

    return map[n]

def number_of_steps_recur(n):

    if n < 0:
        return 0
    if n == 0:
        return 1

    return number_of_steps_recur(n - 1) + number_of_steps_recur(n - 2) + number_of_steps_recur(n - 3)

def main():
    print number_of_steps_recur(20)
    print number_of_steps_dp(20, {0:1})

if __name__ == '__main__':
    main()