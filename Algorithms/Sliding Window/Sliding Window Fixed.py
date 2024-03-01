# Given an array, return true if there are two elements within a window of size k are equal

# optimised approach
# Iterate through the list
# Use a hashmap to store values in window size k
# remove leftmost element when moving window, add right element
# check for condition in the hash set

def sliding_window(nums: list[int],  k: int) -> bool:
    window = set()
    L = 0

    for R in range(len(nums)):
        print(f'Iteration number : {R}')
        if R - L  >= k:
            window.remove(nums[L])
            L += 1

        if nums[R] in window:
            print('match found')
            # return True
        window.add(nums[R])
        print(f'{R} : {window}')

    return False


nums1 = [1, 2, 3, 4, 5, 6]
sliding_window(nums1, k=3)
# assert sliding_window(nums1, k=2) == False
# assert sliding_window(nums1, k=3) == True


# brute force
# Iterate through the list
# Iterate through the window
# Check for condition
def sliding_window_bf(nums: list[int], k: int) -> bool:
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False


nums1 = [1, 2, 3, 2, 3, 4]

assert sliding_window_bf(nums1, k = 2) == False
assert sliding_window_bf(nums1, k = 3) == True



