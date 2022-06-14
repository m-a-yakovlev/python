'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
from collections import defaultdict

def groupAnagrams(strs: 'list[str]') -> 'list[str]':
    result = defaultdict(list)

    for s in strs:
        count = [0] * 26 # a to z -> 26 charachters

        for c in s:
            count[ord(c) - ord('a')] += 1 #ord() -> to get ASCII number of character | chr() -> to get character using ASCII number

        result[tuple(count)].append(s)
    
    return result.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
