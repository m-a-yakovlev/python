# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Solution 1
from collections import Counter

def isAnagram1(s, t):
    return Counter(s) == Counter(t)


# Solution 2
def isAnagram2(s, t):
    return sorted(s) == sorted(t) # str method