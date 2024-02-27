"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas,
she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
"""

# We want koko to eat all the bananas
# 1. To eat all bananas len(piles) <= h hours
# 2. If we take max(piles) as rate koko will always finish the banana in len(piles) hours
# 3. To find minimum the search space is between [1, max(piles)]
# we can do binary search and find the minimum rate in which koko can eat
# initialise ans = max(piles), now do binary search and perform compute func
# compute func : checks if koko can eat all bananas within h hours at selected speed.


def min_rate(piles: list[int], h: int) -> int:

    low = 1
    high = max(piles)
    ans = max(piles)

    while low <= high:
        k = (low + high) // 2
        time = 0
        for i in piles:
            time += i // k
            if i % k != 0:
                time += 1
        if time <= h:
            ans = min(k, ans)
            high = k - 1
        else:
            low = k + 1
    return ans


piles1 = [3, 6, 7, 11]
h1 = 8
assert min_rate(piles1, h1) == 4

piles2 = [312884470]
h2 = 968709470

assert min_rate(piles2, h2) == 1
