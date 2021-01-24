'''
approach 1: Brute Force
Time: O(NlogN), where N is the total number of nodes.
	a. Collecting all the values costs O(N) time.
	b. A stable sorting algorithm costs O(NlogN) time.
	c. Iterating for creating the linked list costs O(N) time.
Space: O(N)
	a. Sorting costs O(N) space(depends on the algorithm you choose)
	b. Creating a new linked list costs O(N) space.

ref:
https://leetcode.com/problems/merge-k-sorted-lists/solution/

You are here!
Your runtime beats 97.43 % of python submissions
You are here!
Your memory usage beats 42.23 % of python submissions.
'''


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
        values = []
        head = node = ListNode()
        
        for li in lists:
            while li:
                values.append(li.val)
                li = li.next
        
        values.sort()
        
        for value in values:
            node.next = ListNode(value)
            node = node.next
        
        return head.next
    