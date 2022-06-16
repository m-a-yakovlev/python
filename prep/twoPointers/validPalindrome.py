'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
'''
# Solution 1
def isPalindrome1(s: str) -> bool:
    filtered_s = list(map(lambda x: x.lower(), filter(lambda x: x.isalnum(), s)))

    return filtered_s == filtered_s[::-1]


# Solution 2
def isPalindrome2(s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not alphanum(s[l]):
                l += 1
            while l < r and not alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    
def alphanum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
