def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k



###################################################

def removeDuplicates(nums):
    l = 1
    r = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[l] = nums[i]
            l += 1
        r += 1
    print(l)
    print(nums)
        
    return l, nums


#nums1 = [1,1,2]
# 2, nums = [1,2,_]
#nums2 = [0,0,1,1,1,2,2,3,3,4,4]
# 5, nums = [0,1,2,3,4,_,_,_,_,_]
#removeDuplicates(nums1)
#removeDuplicates(nums2)

######################################################
'''
def rotate(nums: list[int], k: int) -> None:
    for i in range(len(nums)):
        nums[i-1], nums[i] = nums[i], nums[i+1]
        print(nums)



nums3 = [1,2,3,4,5,6,7]
k3 = 3
nums4 = [-1,-100,3,99]
k4 = 2
rotate(nums3, k3)
rotate(nums4, k4)
'''

#########################################

def sortedSquares(nums: list[int]) -> list[int]:
    answer = []    
    l, r = 0, len(nums)-1
    
    while l <= r:
        if nums[l]**2 > nums[r]**2:
            answer.append(nums[l]**2)
            l += 1
        else:
            answer.append(nums[r]**2)
            r -= 1
    
    return answer[::-1]

print(sortedSquares([-5,-3,-2,-1]))


############################################

def duplicateZeros(arr: list[int]) -> None:
    i = 0
    while i < len(arr):
        if arr[i] != 0:
            i += 1
        else:
            arr.insert(i+1, 0)
            arr.pop()
            i += 2
    return arr

print(duplicateZeros([1,0,0,0,1,2,3,4,0,1,1,1]))



############################################

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    last = m + n - 1
    while m > 0 and n > 0:
        if nums2[n-1] > nums1[m-1]:
            nums1[last] = nums2[n-1]
            n -= 1
        else:
            nums1[last] = nums1[m-1]
            m -= 1
        last -= 1
    while n > 0:
        nums1[last] = nums2[n-1]
        n -= 1
        last -= 1

    return nums1


print(merge([1],1, [], 0))

    
####################################

def validMountainArray(arr: list[int]) -> bool:
    pass



validMountainArray([2,0,2])

# 0x91ca579b0d47e5cfd5d0862c21d5659d39c8ecf0n


#Rotation Point: Binary Search -> Codecademy

# find rotation point
# O(logN) time requirement
# return index of "rotation point" element

def rotation_point(rotated_list):
  left = 0
  right = len(rotated_list) - 1
  while left <= right:
    mid = (left + right) // 2
    mid_next = (mid + 1) % len(rotated_list)
    mid_previous = (mid - 1) % len(rotated_list)

    if rotated_list[mid] < rotated_list[mid_next] and rotated_list[mid] < rotated_list[mid_previous]:
      return mid
    elif rotated_list[mid] < rotated_list[right]:
      right = mid - 1
    else:
      left = mid + 1

"""
#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(
    ['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(
    ['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(
    [13, 8, 9, 10, 11]), 1, rotation_point([13, 8, 9, 10, 11]) == 1))
"""

def rotate(nums, k):
        new_nums = nums[-k-1:] + nums[:k]
        nums = new_nums[:]
        return nums


print('\n')


def replaceElements(arr):
    r = arr[-1]
    print(r)
    for i in range(len(arr)-1, 0, -1):
        print(i)
        if arr[i] >= arr[i-1]:
            print("if: " + str(arr[i-1]) + " - " + str(arr[i]))
            r = arr[i]
            print("if: r = " + str(r))
            arr[i-1] = r
            print("if: " + str(arr[i-1]) + " - " + str(arr[i]))
        else:
            r = arr[i-1]
            print("else: r = " + str(r))
            arr[i-1] = r
            print("else: " + str(arr[i-1]) + " - " + str(arr[i]))

    arr[-1] = -1
    return arr


replaceElements([17, 18, 5, 4, 6, 1])
