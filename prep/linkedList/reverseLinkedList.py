'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: 'optional[ListNode]') -> 'optional[ListNode]':
        previous, current = None, head
        
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        return previous
