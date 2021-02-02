'''
approach: Hash Table / Set
Time: O(N), we visit each of the n elements in the list at most once. Adding a node to the hash table costs only O(1) time.
Space: (N). The space depends on the number of elements added to the hash table, which contains at most n elements.


Success
Details 
Runtime: 52 ms, faster than 16.99% of Python online submissions for Linked List Cycle.
Memory Usage: 20.4 MB, less than 11.53% of Python online submissions for Linked List Cycle.
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
        
        nodes_seen = set()
        while head:
            if head in nodes_seen: return True
            nodes_seen.add(head)
            head = head.next
        
        return False
    