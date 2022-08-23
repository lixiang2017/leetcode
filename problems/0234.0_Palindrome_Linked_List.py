'''
Runtime: 878 ms, faster than 85.93% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 46.5 MB, less than 56.58% of Python3 online submissions for Palindrome Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next 
        return arr == arr[:: -1]
        