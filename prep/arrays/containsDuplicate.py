# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Solution 1
def containsDuplicates1(nums) -> bool:
    new = set(nums)
    return len(nums) != len(new)


# Solution 2
def containsDuplicates2(nums):
    nums.sort() #do NOT assign 'nums' to new value -> sort in-place instead. otherwise TypeError -> Object of Type None has no len
    print(len(nums))
    for i in range(1, len(nums)):
        print('i = ' + str(i))
        if nums[i-1] == nums[i]:
            return True
    return False
    

# Solution 3
from collections import Counter

def containsDuplicates3(nums):
    new = dict(Counter(nums)) # key -> initial data; value -> count of initial data
    for i in new.values():
        if i > 1:
            return True
    return False
    
