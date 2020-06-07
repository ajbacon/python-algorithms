def lis(arr):
    n = len(arr)

    max_arr = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            x = 0
            if arr[i] >= arr[j]:
                x = max_arr[j] + 1

            if x > max_arr[i]:
                max_arr[i] = x

    print(max_arr)


# Driver program to test above function
arr = [-1, 3, 4, 5, 2, 2, 2, 2]
print("Length of lis is", lis(arr))
# This code is contributed by Nikhil Kumar Singh

# [3, 1, 2, 3]
# [1, 1, 2, 3]

# [-1, 3, 4, 5, 2, 2, 2, 2]
# [1, 2, 3, 4, 2, 3, 4, 5]
