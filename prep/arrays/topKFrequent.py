# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent(nums, k):
    count = {}
    frq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0) # same as count = dict(Counter(nums))

    for n, c in count.items():
        frq[c].append(n)

    result = []
    for i in range(len(nums)-1, 0, -1):
        for n in frq[i]:
            result.append(n)
            if len(result) == k:
                return result


print(topKFrequent([1,3,5,2,0,0,0,8,6,6,5], 3))
