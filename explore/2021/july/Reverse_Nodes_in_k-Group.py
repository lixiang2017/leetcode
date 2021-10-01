'''
You are here!
Your runtime beats 56.15 % of python3 submissions.
You are here!
Your memory usage beats 10.25 % of python3 submissions.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        dummy = node = ListNode()
        for i in range(0, len(values), k):
            if i + k <= len(values):
                values[i: i + k] = values[i: i + k][:: -1]
                count = k
            else:
                count = len(values) - i
                
            delta = 0
            while count:
                node.next = ListNode(values[i + delta])
                node = node.next
                delta += 1
                count -= 1
                
        return dummy.next


'''
Stack
Time: O(2N) = O(N)
Space: O(k)

You are here!
Your runtime beats 56.15 % of python3 submissions.
You are here!
Your memory usage beats 76.72 % of python3 submissions.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = node = ListNode()
        stack = []
        while head:
            stack.append(head)
            head = head.next
            if len(stack) == k:
                # Error - Found cycle in the ListNode
                stack[0].next = None
                # reverse
                while stack:
                    node.next = stack.pop()
                    node = node.next
        # left in stack, no need to reverse
        if stack:
            node.next = stack[0]
        
        return dummy.next




'''
[1,2,3,4,5]
2
[1,2,3,4,5]
3
[1,2,3,4,5]
1
[1]
1
[3,5]
2
'''



'''
Recursion

#                          nH
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
#                          c
# h
#                      1 c
#                        \
#     2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
#     h
#                  c
#                  2 -> 1
#                        \
#          3 -> 4 -> 5 -> 6 -> 7 -> 8
#          h
#             c
#             3 -> 2 -> 1 
#                        \
#              4 -> 5 -> 6 -> 7 -> 8
#              h

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        nextGroupHead, nodeNum = head, 0
        while nextGroupHead and nodeNum < k:
            nextGroupHead = nextGroupHead.next
            nodeNum += 1
        
        if nodeNum == k:
            # have completed the later part
            newHead = Solution.reverseKGroup(self, nextGroupHead, k)
            curTailNext = newHead
            for _ in range(k):
                nextNode = head.next
                head.next = curTailNext
                curTailNext = head
                head = nextNode   
            head = curTailNext
        
        return head

'''
Iteration
You are here!
Your runtime beats 98.03 % of python3 submissions.
You are here!
Your memory usage beats 45.77 % of python3 submissions.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or not head:
            return head
        
        c, it = 0, head
        while it:
            c, it = c + 1, it.next
        
        it = dummy = ListNode(next = head)
        for _ in range(c // k):
            start, head = head, head.next
            for i in range(1, k):
                it.next, start.next, head.next, head = start.next, head.next, it.next, head.next
            it = start
        return dummy.next
    
