'''
approach: Compare One by One + Priority Queue + [link nodes in place]

Time: O(Nlogk)
Space: O(k) for priorty queue

You are here!
Your runtime beats 36.37 % of python submissions.
You are here!
Your memory usage beats 52.64 % of python submissions.
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
                q.put((li.val, li))
        
        while not q.empty():
            value, node = q.get()
            # point.next = ListNode(value)
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        
        return head.next
    
