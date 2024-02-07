def getprefixscores(arr : list[int]) -> list[int]:
    ans = [0] * len(arr)
    mx = 0
    m = 1e9 + 7
    sumu = 0
    ssum = 0
    for i in range(len(arr)):
        sumu += arr[i]
        print(arr[i])
        sumu %= m
        ssum += sumu
        ssum %= m
        mx = max(mx, arr[i])
        print(sumu,ssum,mx)
        ans[i] = ssum + mx * (i + 1) % m
        print(ans[i])
        # ans[i] = int(ans[i] % m)
    return ans


nums = [1, 2, 3]
print(getprefixscores(nums))
print(1e9 + 7)
