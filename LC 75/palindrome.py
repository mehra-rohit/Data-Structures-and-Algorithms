# LC 125 Valid Palindrome
# after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters
# string is palindrome or not


def palindrome(string: str) -> bool:
    # string cleanup
    string_cleaned = ''
    for i in string.lower():
        if i.isalnum():
            string_cleaned += i

    # #check for palindrome
    # for i in range(len(string_cleaned)):
    #     if i > len(string_cleaned) // 2:
    #         break
    #     if string_cleaned[i] == string_cleaned[len(string_cleaned)-1-i]:
    #         continue
    #     else:
    #         return False

    # using while loop
    l, r = 0, len(string_cleaned) - 1
    while l < r:
        if string_cleaned[l] == string_cleaned[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


s = "A man, a plan, a canal: Panama"
print(palindrome(s))


# nums array is palindrome or not
# Approach: Iterate through nums and check if first and last are same, repeat with
# first+1 and last-1 index

def valid_palindrome(nums: list[int]) -> bool:
    for i in range(len(nums)):
        if i > len(nums) // 2:
            break
        if nums[i] == nums[len(nums) - 1 - i]:
            continue
        else:
            return False
    return True


nums1 = [1, 2, 3, 4, 3, 2, 1]
nums2 = [1, 2, 3, 3, 2, 1]
nums3 = [1, 5, 4, 3, 2, 1]

assert valid_palindrome(nums1) == True
assert valid_palindrome(nums2) == True
assert valid_palindrome(nums3) == False
