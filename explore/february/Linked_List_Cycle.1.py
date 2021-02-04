'''
approach: Hash Table / Set
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 99.33 % of python submissions.
You are here!
Your memory usage beats 18.88 % of python submissions.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False
        
        seen = set()
        while head:
            if head in seen: return True
            seen.add(head)
            head = head.next
        
        return False


'''
You are here!
Your runtime beats 65.54 % of python submissions.

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False
        
        seen = defaultdict(bool)
        while head:
            if head in seen: return True
            seen[head] = True
            head = head.next
        
        return False
    