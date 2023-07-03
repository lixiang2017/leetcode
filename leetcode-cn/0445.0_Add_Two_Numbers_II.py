'''
stack + link list reverse (头插法)
T: O(M + N)
S: O(M + N)

执行用时：76 ms, 在所有 Python3 提交中击败了10.08% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了60.12% 的用户
通过测试用例：1563 / 1563
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next 
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        another = None 
        carry = 0
        while stack1 or stack2 or carry:
            s = carry
            if stack1:
                s += stack1.pop()
            if stack2:
                s += stack2.pop()
            carry, x = divmod(s, 10)
            node = ListNode(x, another)
            another = node 

        return another


'''
stack 

执行用时：92 ms, 在所有 Python3 提交中击败了8.26% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了50.00% 的用户
通过测试用例：1563 / 1563
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1)
            l1 = l1.next 
        while l2:
            stack2.append(l2)
            l2 = l2.next 

        current, carry = None, 0
        while stack1 or stack2 or carry:
            _sum = carry 
            if stack1:
                _sum += stack1.pop().val 
            if stack2:
                _sum += stack2.pop().val 
            carry, _sum = divmod(_sum, 10)
            current = ListNode(_sum, current)
        return current
       


