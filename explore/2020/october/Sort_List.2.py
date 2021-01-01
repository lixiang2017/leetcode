'''
You are here!
Your runtime beats 47.34 % of python submissions.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """     
        def merge_sorted(list1, list2):
            cur1 = list1
            cur2 = list2
            head = ListNode(0)
            cur = head
            
            while cur1 and cur2:
                if cur1.val < cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                cur = cur.next
            
            if not cur1:
                cur.next = cur2
            else:
                cur.next = cur1
                
            return head.next
        
        
        if not head or not head.next:
            return head
        
        fast = head
        slow = head
        pre_slow = None
        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        pre_slow.next = None   # to cut the link
        
        return merge_sorted(self.sortList(head), self.sortList(slow))
            
