'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

# Solution 1
def twoSum(nums, target):
    for i in range(len(nums)):
        for k in range(i+1, len(nums)):
            if nums[i] + nums[k] == target and i != k:
                return [i, k]


# Solution 2
def twoSum(nums, target):
    hm = {}
    for i in range(len(nums)):
        if (target - nums[i]) in hm:
            return [hm[target-nums[i]], i]
        hm[nums[i]] = i
