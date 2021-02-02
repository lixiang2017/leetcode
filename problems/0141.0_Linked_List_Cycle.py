'''
approach: Floyd's Cycle Finding Algorithm / Slow and Fast Pointers
Time: O(N)
Space: O(1)

Success
Details 
Runtime: 40 ms, faster than 65.28% of Python online submissions for Linked List Cycle.
Memory Usage: 19.7 MB, less than 46.39% of Python online submissions for Linked List Cycle.
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
        while slow and fast:
            if slow == fast: return True
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next
        
        return False



'''
Success
Details 
Runtime: 52 ms, faster than 16.99% of Python online submissions for Linked List Cycle.
Memory Usage: 19.5 MB, less than 94.57% of Python online submissions for Linked List Cycle.
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
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True
        

'''
Success
Details 
Runtime: 52 ms, faster than 16.99% of Python online submissions for Linked List Cycle.
Memory Usage: 19.9 MB, less than 33.91% of Python online submissions for Linked List Cycle.
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
            # if not fast or not fast.next:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True
        
    