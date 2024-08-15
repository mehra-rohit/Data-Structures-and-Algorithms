'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.
'''

from typing import List

nums = [1,2,2,3,3,3]
k = 2

# time-> O(n), Space -> O(n)
def topKFrequent(nums: List[int], k: int) -> List[int]:
    topk = []
    # compute frequency of each number
    freq = {}
    for n in nums:
        freq[n] = freq.get(n,0) + 1
    
    # treat frequency as index and maintain a list of numbers there
    ans = [[] for i in range(len(nums)+1)]

    for n in freq:
        ans[freq[n]].append(n)

    # iterate in reverse and fetch k numbers
    for i in range(len(ans)-1,-1,-1):
        for j in ans[i]:
            topk.append(j)
            if len(topk) == k:
                return topk

assert topKFrequent(nums, k) == [3, 2]