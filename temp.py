def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    n = len(cost)
    t = [-1 for i in range(n + 1)]
    t[0] = cost[0]
    t[1] = cost[1]

    for i in range(2, n + 1):
        if i == n:
            ti = min(t[i - 1], t[i - 2])
        else:
            t[i] = cost[i] + min(t[i - 1], t[i - 2])
        t.append(ti)
    return t

print(minCostClimbingStairs([1,2,3,100,1,2,1]))