def product_except_self(nums: list[int]) -> list[int]:

    prp = 1  # preproduct variable
    pop = 1  # postproduct variable
    res = [1]*len(nums) # to process and store product of array except self

    # computing preproduct and storing in res with 1 index lag
    for i in range(len(nums)):
        res[i] *= prp
        prp *= nums[i]

    # computing postproduct and updating res with 1 index lag
    for i in range(len(nums)-1, -1, -1):
        res[i] *= pop
        pop *= nums[i]

    return res


nums1 = [1, 2, 3]
assert product_except_self(nums1) == [6, 3, 2]

