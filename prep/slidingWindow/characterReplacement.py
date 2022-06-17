'''
You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

# Solution 1
def characterReplacement(s: str, k: int) -> int:
    count = {}
    result = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        #while our window in NOT valid (amount of characters minus couhnt of most repeated character in window is greater than k)
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        result = max(result, r - l + 1)

    return result


print(characterReplacement())


# Solution 2
def characterReplacement2(s: str, k: int) -> int:
    count = {}
    result = 0
    maxFreq = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxFreq = max(maxFreq, count[s[r]])

        #while our window in NOT valid (amount of characters minus couhnt of most repeated character in window is greater than k)
        while (r - l + 1) - maxFreq > k:
            count[s[l]] -= 1
            l += 1

        result = max(result, r - l + 1)

    return result
