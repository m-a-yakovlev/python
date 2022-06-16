'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
'''

def longestConsecutive(nums: 'list[int]') -> int:
    if not nums:
        return 0
    
    numset = set(nums)

    current = 1

    for n in nums:
        if (n - 1) not in numset:
            longest = 1
            nex = n + 1

            while nex in numset:
                longest += 1
                nex += 1
            
            current = max(current, longest)

    return current

        
print(longestConsecutive([-100, 0, 1, -1, 5, 6, 9, -2, 4, 10, 11, -3]))
