'''
approach 4: Merge Lists One by One
Convert merge k lists problem to merge 2 lists (k - 1) times.
Time: O(k * N) where k is the number of linked lists.
Space: O(1)

You are here!
Your runtime beats 8.61 % of python submissions.
You are here!
Your memory usage beats 62.83 % of python submissions.
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
        head = None
        for li in lists:
            head = self.merge2Lists(head, li)
        return head
    
    def merge2Lists(self, list1, list2):
        head = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
                node = node.next
            else:
                node.next = list2
                list2 = list2.next
                node = node.next
        
        if list1: node.next = list1
        if list2: node.next = list2
        
        return head.next
    