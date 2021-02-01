'''
Time: O(M + N), M is the length of l1 and N is the length of l2.
Space: O(1), use the original memory of l1 and l2, just change pointers

执行结果：
通过
显示详情
执行用时：48 ms, 在所有 Python 提交中击败了93.32%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了7.14%的用户
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = node = ListNode()
        while l1 or l2:
            total = carry
            pre_l1, pre_l2 = l1, l2
            if l1: 
                total += l1.val
                l1 = l1.next
            if l2: 
                total += l2.val
                l2 = l2.next

            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0
            
            
            if pre_l1:
                node.next = pre_l1
                pre_l1.val = total
                node = node.next
            elif pre_l2:
                node.next = pre_l2
                pre_l2.val = total
                node = node.next
        
        if carry:
            node.next = ListNode(val=carry)
        
        return dummy.next
