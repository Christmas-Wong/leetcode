def integer_break_dp(n):
    n += 1
    dp = [1 for x in range(n)]
    for i in range(1, n):
        for j in range(1, n-i):
            if i+j < n:
                dp[i+j] = find_max(dp[i+j], find_max(i, dp[i])*find_max(j, dp[j]))
    return dp


def find_max(a, b):
    if a > b:
        return a
    return b


def greedy_algorithm(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    max_value = 1
    while n >= 5:
        max_value *= 3
        n -= 3
    max_value *= n
    return max_value


if __name__ == "__main__":
    print(integer_break_dp(10))
    print(greedy_algorithm(10))