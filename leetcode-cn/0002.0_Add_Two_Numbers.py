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



'''
熟练之后，写的代码越来越精炼了。
2021-09-05

执行用时：52 ms, 在所有 Python3 提交中击败了86.56% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了38.40% 的用户
通过测试用例：1568 / 1568
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = node = ListNode()
        while l1 or l2:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = divmod(total, 10)
            node.next = ListNode(val)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            node.next = ListNode(carry)

        return dummy.next


'''
recursion


执行用时：56 ms, 在所有 Python3 提交中击败了84.18% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了13.74% 的用户
通过测试用例：1568 / 1568
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None 
        if l1 is None:
            l1, l2 = l2, l1 
        carry += l1.val  + (l2.val if l2 else 0)
        l1.val = carry % 10 
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, carry // 10)
        return l1 

