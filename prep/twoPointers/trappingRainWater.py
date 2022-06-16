'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
'''
def trap(height: 'list[int]') -> int:
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    result = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max((leftMax, height[l]))
            result += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            result += rightMax - height[r]
    
    return result


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
