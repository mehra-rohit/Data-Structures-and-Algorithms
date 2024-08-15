'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''

from typing import List

strs = ["act","pots","tops","cat","stop","hat"]


def is_anagram(s: str, t: str) -> bool:

    return sorted(s) == sorted(t)

# time -> O(n2 * nlogn), Space -> O(n)
def groupAnagrams(strs: List[str]) -> List[List[str]]:

    strs_copy = strs
    ans = []
    to_check = []

    for i,str1 in enumerate(strs_copy):
        if i in to_check:
            continue
        temp = [str1]
        for j in range(i+1, len(strs_copy)):
            if is_anagram(str1, strs_copy[j]) == True:
                temp.append(strs_copy[j])
                to_check.append(j)
        ans.append(temp)
    return ans

# Expected output
expected_output = [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
result = groupAnagrams(strs)
result_sorted = sorted([sorted(group) for group in result])
expected_output_sorted = sorted([sorted(group) for group in expected_output])
assert result_sorted == expected_output_sorted

assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["x"]) == [["x"]]


# dictionary approach
# time -> O(n*nlogn), Space -> O(n)
def groupAnagrams(strs: List[str]) -> List[List[str]]:

    ans = {}  

    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s in ans:
            ans[sorted_s].append(s)
        else:
            ans[sorted_s] = [s]

    return list(ans.values())


# Expected output
expected_output = [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
result = groupAnagrams(strs)
result_sorted = sorted([sorted(group) for group in result])
expected_output_sorted = sorted([sorted(group) for group in expected_output])
assert result_sorted == expected_output_sorted

assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["x"]) == [["x"]]


# dictionary approach optimised
# time -> O(n*nlogn), Space -> O(n)
def groupAnagrams(strs: List[str]) -> List[List[str]]:

    ans = {}  # Use a dictionary to store grouped anagrams

    for s in strs:
        vec = [0] * 26  # Vector to count frequency of each character
        for i in s:
            vec[ord(i) - ord('a')] += 1  # Increment position corresponding to the character
        vec_tuple = tuple(vec)  # Convert list to tuple to use as a key
        if vec_tuple in ans:
            ans[vec_tuple].append(s)  # Append to the existing list
        else:
            ans[vec_tuple] = [s]  # Create a new list for this key

    return list(ans.values())  # Return the grouped anagrams as a list of lists

# Expected output
expected_output = [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
result = groupAnagrams(strs)
result_sorted = sorted([sorted(group) for group in result])
expected_output_sorted = sorted([sorted(group) for group in expected_output])
assert result_sorted == expected_output_sorted

assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["x"]) == [["x"]]