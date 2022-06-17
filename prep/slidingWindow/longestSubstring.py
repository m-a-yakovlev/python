'''
Given a string s, find the length of the longest substring without repeating characters.
'''


def lengthOfLongestSubstring(s: str) -> int:
    sSet = set()
    result = 0
    l = 0
    for r in range(len(s)):
        while s[r] in sSet:
            sSet.remove(s[l])
            l += 1
        
        sSet.add(s[r])
        result = max(result, r - l + 1)

    return result

    

print(lengthOfLongestSubstring('abcabcbb'))
