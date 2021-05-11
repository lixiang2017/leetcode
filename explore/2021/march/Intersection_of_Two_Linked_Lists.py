'''
approach: Hash Set
Time: O(M + N)
Space: (M)

You are here!
Your runtime beats 92.49 % of python submissions.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptrA, ptrB, seen = headA, headB, set()
        while ptrA:
            seen.add(ptrA)
            ptrA = ptrA.next
        
        while ptrB:
            if ptrB in seen:
                return ptrB
            ptrB = ptrB.next
        return None




'''
approach: Two Pointers
Time: O(M + N)
Space: O(1)

You are here!
Your runtime beats 92.49 % of python submissions.
You are here!
Your memory usage beats 55.64 % of python submissions.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p
