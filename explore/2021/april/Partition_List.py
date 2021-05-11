'''
approach: One Pointer
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 54.68 % of python3 submissions.
You are here!
Your memory usage beats 95.36 % of python3 submissions.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from itertools import chain

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # less than, greater than or equal to 
        lt, ge = [], []
        ahead = head
        while ahead:
            if ahead.val < x:
                lt.append(ahead.val)
            else:
                ge.append(ahead.val)
            old_head = ahead
            ahead = ahead.next
            del old_head
            
        # construct a new singly-linked list
        # dummy = node = ListNode(next=None)
        dummy = node = ListNode()
        for value in chain(lt, ge):
            node.next = ListNode(val=value)
            node = node.next
        return dummy.next



'''
approach: Two Pointers
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 54.68 % of python3 submissions.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyless = less = ListNode()
        dummymore = more = ListNode()
        
        while head:
            if head.val < x:
                less.next = head
                less = head
            else:
                more.next = head
                more = head
            head = head.next
            
        less.next = dummymore.next
        more.next = None
        return dummyless.next
    