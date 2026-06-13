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

def print_ways(n, k):
    powers = []
    x = 1
    while (p := x ** k) <= n:
        powers.append(p)
        x += 1

    ways = []

    def dfs(i, rem, path):
        if rem == 0:
            ways.append(path[:])
            return

        if rem < 0 or i == len(powers):
            return

        # Skip current power
        dfs(i + 1, rem, path)

        # Take current power
        path.append(powers[i])
        dfs(i + 1, rem - powers[i], path)
        path.pop()

    dfs(0, n, [])

    for idx, way in enumerate(ways, 1):
        print(f"Way {idx}: {' + '.join(map(str, way))} = {n}")

    return ways


# Example
print_ways(100, 2)

print(count_ways(17, 3))  # 2
print(count_ways(15, 2))  # 4