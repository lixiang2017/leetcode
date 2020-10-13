'''
You are here!
Your runtime beats 86.47 % of python submissions.
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
        if not head:
            return None
        
        array = []
        while head:
            array.append(head.val)
            head = head.next
         
        #array = sorted(array)
        array.sort()
        print 'array: ', array
        
        head_val = array.pop(0)
        head = ListNode(val=head_val)
        new_head = head
        while array:
            left_value = array.pop(0)
            new_node = ListNode(val=left_value)
            head.next = new_node
            head = head.next
        
        return new_head
        