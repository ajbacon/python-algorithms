def ssgs(arr, val):
    n = val + 1
    m = len(arr)

    dp = [[0 for x in range(n)] for y in range(m)]
    # base cases
    for i in range(m):
        dp[i][0] = 1

    dp[0][arr[0]] = arr[0]

    for i in range(1, m):
        for j in range(1, n):
            # 2 cases
            # a) use the value
            # b) don't use the value

            a = dp[i - 1][j]
            b = dp[i - 1][j - arr[i]] if j - arr[i] >= 0 else 0
            dp[i][j] = a + b

    print(dp)


ssgs([1, 2, 4, 5], 7)
