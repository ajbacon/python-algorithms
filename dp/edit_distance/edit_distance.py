def edit_distance(A, B):

    n = len(A) + 1
    m = len(B) + 1

    dp = [[0 for el in range(n)] for el in range(m)]

    for i in range(1, n):
        dp[0][i] = i

    for i in range(1, m):
        dp[i][0] = i

    for i in range(1, m):
        for j in range(1, n):
            min_changes = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

            dp[i][j] = min_changes if A[i - 1] == B[j - 1] else min_changes + 1

    print(dp)

    return dp[m - 1][n - 1]


print(edit_distance('cat', 'dog'))
print(edit_distance('cat', 'bat'))
