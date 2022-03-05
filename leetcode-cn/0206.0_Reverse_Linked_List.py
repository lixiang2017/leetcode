'''
iteration,  头插法
T: O(N)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了48.66% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了39.48% 的用户
通过测试用例：28 / 28
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        another
        head/first -> second -> third -> ...
        '''
        another, node = None, head
        while node:
            next_part = node.next 
            # link
            node.next = another 
            # set new head
            another = node 
            # move to next part
            node = next_part

        return another 
        

'''
iteration,  头插法
T: O(N)
S: O(1)

执行用时：52 ms, 在所有 Python3 提交中击败了10.41% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了49.98% 的用户
通过测试用例：28 / 28
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        another, node = None, head
        while node:
            node.next, another, node = another, node, node.next 
        return another 



'''
recursion
T: O(N)
S: O(N)

执行用时：56 ms, 在所有 Python3 提交中击败了10.41% 的用户
内存消耗：20.7 MB, 在所有 Python3 提交中击败了7.24% 的用户
通过测试用例：28 / 28
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # return real tail node
        if not head or not head.next:
            return head 
        tail = self.reverseList(head.next)
        # for every current node
        head.next.next = head 
        head.next = None
        return tail

'''
stack + dummy node
T: O(2N)
S: O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了25.07% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了32.75% 的用户
通过测试用例：28 / 28
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack, node = [], head 
        while node:
            next_part = node.next
            node.next = None 
            stack.append(node)
            node = next_part
        dummy = node = ListNode()
        while stack:
            node.next = stack.pop()
            node = node.next 
        return dummy.next 

'''
stack 2 + dummy node
T: O(2N)
S: O(N)

执行用时：52 ms, 在所有 Python3 提交中击败了10.41% 的用户
内存消耗：16.7 MB, 在所有 Python3 提交中击败了24.46% 的用户
通过测试用例：28 / 28
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack, node = [], head 
        while node:
            stack.append(node.val)
            node = node.next 
        dummy = node = ListNode()
        while stack:
            node.next = ListNode(stack.pop())
            node = node.next 
        return dummy.next 





