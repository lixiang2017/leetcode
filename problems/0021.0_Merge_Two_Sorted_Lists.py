'''
Success
Details
Runtime: 24 ms, faster than 80.09% of Python online submissions for Merge Two Sorted Lists.
Memory Usage: 13.2 MB, less than 13.68% of Python online submissions for Merge Two Sorted Lists.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1, head2 = l1, l2
        dummy = ListNode(-1)
        current = dummy
        
        while head1 and head2:
            if head1.val < head2.val:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
        
        if not head1:
            current.next = head2
        if not head2:
            current.next = head1
        
        return dummy.next


'''
iteration

Runtime: 32 ms, faster than 97.89% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14 MB, less than 60.85% of Python3 online submissions for Merge Two Sorted Lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        hair = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next 
        
        if list1:
            node.next = list1
        if list2:
            node.next = list2
        
        return hair.next 
        
'''
recursion

Runtime: 32 ms, faster than 97.89% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14 MB, less than 60.85% of Python3 online submissions for Merge Two Sorted Lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        

        
