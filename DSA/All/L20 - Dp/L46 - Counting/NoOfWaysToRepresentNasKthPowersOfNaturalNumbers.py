# Number of ways to represent N as sum of Kth powers of natural numbers

def countWaysUtil(n, k, maxNum):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if k == 1:
        return 1 if n <= maxNum else 0

    ways = 0
    for i in range(1, maxNum + 1):
        ways += countWaysUtil(n - i**k, k, i)

    return ways


# highly space taking
def count_ways(n, k):
    powers = [i**k for i in range(1, int(n**(1/k)) + 2) if i**k <= n]

    dp = [0] * (n + 1)
    dp[0] = 1

    for p in powers:
        for s in range(p, n + 1):
            dp[s] += dp[s - p]

    return dp[n]