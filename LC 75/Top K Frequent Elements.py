# def top_k_element(nums: list[int], k: int) -> list[int]:
#     temp = {}
#     for i in nums:
#         # if i in temp:
#         #     temp[i] += 1
#         # else:
#         #     temp[i] = 1
#         temp[i] = temp.get(i,0) + 1
#     ans = sorted(temp, key=temp.get, reverse=True)[:k]
#     return ans

def top_k_element(nums: list[int], k: int) -> list[int]:
    count_dict = {}
    ans = []

    # store element count in dict
    for element in nums:
        count_dict[element] = count_dict.get(element, 0) + 1

    bucket = [[] for i in range(len(nums)+1)]

    for element, count in count_dict.items():
        bucket[count].append(element)

    for i in range(len(bucket)-1, 0, -1):
        for element in bucket[i]:
            ans.append(element)
            if len(ans) == k:
                return ans


nums_ = [1, 1, 1, 2, 2, 3]
k_ = 2
assert top_k_element(nums_, k_) == [1,2]
assert top_k_element(nums_,3) == [1, 2, 3]


nums2 = [2, 2, 2, 3, 3, 4]
k2 = 2
assert top_k_element(nums2, k2) == [2,3]

