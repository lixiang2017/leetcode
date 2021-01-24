'''
approach: Compare One by One + Priority Queue
Time: O(Nlogk) where k is ther number of linked lists.
	a. The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue.
	   But finding the node with the smallest value just costs O(1) time.
	b. There are N nodes in the final linked list.
Space: 
	a. O(n) Creating a new linked list costs O(n) space.


Success
Details 
Runtime: 168 ms, faster than 23.47% of Python online submissions for Merge k Sorted Lists.
Memory Usage: 23.3 MB, less than 9.07% of Python online submissions for Merge k Sorted Lists.

'''


from Queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode()
        q = PriorityQueue()
        for li in lists:
            if li:
                # q.put((li, li.val))   # wrong! 
                q.put((li.val, li))
        
        while not q.empty():
            # node, value = q.get()
            value, node = q.get()
            point.next = ListNode(value)
            point = point.next
            node = node.next
            if node:
                # q.put((node, node.val))
                q.put((node.val, node))
        
        return head.next
    