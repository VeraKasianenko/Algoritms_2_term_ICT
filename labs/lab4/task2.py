dims = [3, 2, 2, 4]
print(dims)
n = len(dims)
cost = [[0 for i in range(n + 1)] for j in range((n + 1))]
for lenth in range(2, n):
    for l in range(1, n - lenth + 2):
        r = l + lenth - 1
        cost[l][r] = 10000000
        if r < n:
            for m in range(l,r):
                new_cost = cost[l][m] + cost[m + 1][r] + dims[l - 1] * dims[m] * dims[r]
                cost[l][r] = min(cost[l][r], new_cost)
print(cost[1][n - 1])