"""
Given a string s, find the length of the longest
substring without repeating characters.
"""
import string

"""
Sliding Window Variable
0. Use set = store the characters 
1. Iterate over string
2. Check for condition and update pointers
    -> compute curr_string
    -> check if set(longest string) has curr_char
        -> remove while the char exists
    -> else update longset string
        
Note: Maximisation problem so initialize minimum val possible
"""


def long_substring(s: string) -> int:
    L = 0
    long_s = 0
    for R in range(len(s)):
        while s[R] in set(s[L:R]):
            L += 1
        long_s = max(long_s, R - L + 1)
    return long_s

def long_substring(s: string) -> int:
    L = 0
    long_s = 0
    char_set = set()
    for R in range(len(s)):
        while s[R] in char_set:
            char_set.remove(s[L])
            L += 1
        char_set.add(s[R])
        long_s = max(long_s, R - L + 1)
    return long_s



assert long_substring('bbbbb') == 1
assert long_substring('abcabc') == 3
assert long_substring('abcabcbb') == 3
assert long_substring('ynyo') == 3
