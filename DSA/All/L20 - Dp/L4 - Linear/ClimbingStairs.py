# No of ways to climb nth stair with 1 or 2 steps at a time

def climbStairs(n):
    if n < 4: return n
    prev, curr = 2, 3
    for _ in range(n - 4):
        prev, curr = curr, prev + curr
    return curr