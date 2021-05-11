'''
approach: Slow & Fast Pointers
Time: O(N), where N is the number of nodes.
Space: O(1)

You are here!
Your runtime beats 10.46 % of python submissions.
You are here!
Your memory usage beats 65.09 % of python submissions.
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
        if not head: return False
        slow, fast = head, head.next
        
        while slow != fast:
            if not fast or not fast.next: return False
            slow = slow.next
            fast = fast.next.next
        
        return True

'''
You are here!
Your runtime beats 96.07 % of python submissions.
You are here!
Your memory usage beats 46.56 % of python submissions.
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
        slow, fast = head, head.next
        
        while slow and fast:
            if slow == fast: return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False
        return False
