# construct n from k-th powers of unique natural numbers

def can_express(n, k):
    powers = [i**k for i in range(1, int(n**(1/k)) + 2) if i**k <= n]

    dp = [False] * (n + 1)
    dp[0] = True

    for p in powers:
        for s in range(p, n + 1):
            dp[s] |= dp[s - p]

    return dp[n]


print(can_express(17, 3))  # True
print(can_express(15, 2))  # True
print(can_express(15, 3))  # False

from functools import lru_cache

def can_express(n, k):
    powers = []
    x = 1
    while (p := x ** k) <= n:
        powers.append(p)
        x += 1

    @lru_cache(None)
    def dfs(i, rem):
        if rem == 0:
            return True
        if rem < 0 or i == len(powers):
            return False

        return dfs(i + 1, rem) or dfs(i + 1, rem - powers[i])

    return dfs(0, n)


print(can_express(100, 2))