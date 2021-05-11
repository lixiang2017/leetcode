'''
approach 5: Merge2Lists + Divide and Conquer
Time: O(Nlogk)
Space: O(1)

You are here!
Your runtime beats 83.81 % of python submissions.
You are here!
Your memory usage beats 97.43 % of python submissions.
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
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0] if amount > 0 else None
    
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
    
