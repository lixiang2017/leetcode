'''
Runtime: 162 ms, faster than 91.14% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.8 MB, less than 37.81% of Python3 online submissions for Intersection of Two Linked Lists.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a or b:
            if a == b:
                return a 
            if a:
                a = a.next 
            else:
                a = headB
            if b:
                b = b.next 
            else:
                b = headA
        
        return None 


'''
Runtime: 311 ms, faster than 7.75% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 30.3 MB, less than 5.78% of Python3 online submissions for Intersection of Two Linked Lists.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        nodes = set()
        while a:
            nodes.add(a)
            a = a.next
        while b:
            if b in nodes:
                return b 
            b = b.next
            
        return None 

        