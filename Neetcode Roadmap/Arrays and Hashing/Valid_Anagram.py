'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''

s = "racecar"
t = "carrace"

# Time -> O(nlogn), Space -> O(n) (to store the sorted values)
def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False 

    return sorted(s) == sorted(t)

assert isAnagram(s, t) == True

# Time -> O(n), Space -> O(k) (to store the temp dict, k -> number of unique elements)
def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False 
    
    temp = {}

    for i in s:
        temp[i] = temp.get(i, 0) + 1
    
    for j in t:
        temp[j] = temp.get(j, 0) - 1

    return sum(temp.values()) == 0

assert isAnagram(s, t) == True