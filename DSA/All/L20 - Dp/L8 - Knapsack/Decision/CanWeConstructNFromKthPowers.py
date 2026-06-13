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