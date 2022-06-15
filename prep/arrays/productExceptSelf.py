'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
'''

def productExceptSelf(nums):
    result = [1] * (len(nums))

    prefix, postfix = 1, 1

    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]

    for i in range(len(nums)-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result

print(productExceptSelf([125, -3, 5, 0.5, 500, -8]))
