'''
You are given an integer array height of length n.
Find two lines that together with the x-axis form a container, such that the container contains the most water.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
'''

def maxArea(nums: 'list[int]') -> int:
    result = 0 
    l, r = 0, len(nums) - 1
    while l < r:
        area = (r - l) * min(nums[l], nums[r])
        result = max(result, area)
        if nums[l] <= nums[r]:
            l += 1
        else:
            r += 1
    return result


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
