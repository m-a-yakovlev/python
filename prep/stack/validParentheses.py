'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''



def isValid(s: str) -> bool:
    stack = []
    variations = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in variations:
            if stack and stack[-1] == variations[c]:
                stack.pop()

            else:
                return False

        else:
            stack.append(c)

    return True if not stack else False
