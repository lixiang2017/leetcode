'''
approach: Get the length of list / Two Pass Algorithm / One Pointer
Time: O(N + N) = O(N)
Space: O(1)

You are here!
Your memory usage beats 48.74 % of python3 submissions.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(node: ListNode) -> int:
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        length = getLength(head)
        dummy = ListNode(next=head)
        # cur = head  # wrong!  AttributeError: 'NoneType' object has no attribute 'next'
        cur = dummy
        for _ in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        
        return dummy.next

'''
[1]
1
'''



'''
approach: Two Pointers / One Pass Algorithm
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 74.43 % of python3 submissions.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:  
        dummy = ListNode(next=head)
        first = second = dummy
        i = 0
        while i <= n:
            first = first.next
            i += 1
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return dummy.next

'''
approach: Stack
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 74.43 % of python3 submissions.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        stack = []
        dummy = ListNode(next=head)
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        
        for _ in range(n):
            stack.pop()
        
        stack[-1].next = stack[-1].next.next
        
        return dummy.next
        


