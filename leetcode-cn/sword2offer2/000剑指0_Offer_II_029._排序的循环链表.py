'''
执行用时：48 ms, 在所有 Python3 提交中击败了29.99% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了13.34% 的用户
通过测试用例：106 / 106
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            n = Node(insertVal)
            n.next = n 
            return n 

        # or just one node 
        if head == head.next:
            head.next = Node(insertVal, head)
            return head

        # find the point of its max val <= insertVal
        exact_p = None
        # if insertVal < all vals, insert behind max value
        min_val = max_val = head.val 
        max_p = head 
        if head.val <= insertVal:
            exact_p = head 
        slow = head.next
        while slow != head:
            if slow.val <= insertVal:
                if not exact_p or exact_p.val <= slow.val:
                    exact_p = slow 
            # 
            min_val = min(min_val, slow.val)
            if slow.val >= max_val:
                max_val = slow.val 
                max_p = slow 
            # move to next 
            slow = slow.next 

        if insertVal > max_val or insertVal <= min_val:
            next_n = max_p.next 
            max_p.next = Node(insertVal, next_n)
            # return max_p
        else:
            next_n = exact_p.next 
            exact_p.next = Node(insertVal, next_n)
            # return exact_p
        return head 


'''
# or just one node # i guess it's no use

执行用时：44 ms, 在所有 Python3 提交中击败了58.58% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了54.38% 的用户
通过测试用例：106 / 106
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            n = Node(insertVal)
            n.next = n 
            return n 

        # find the point of its max val <= insertVal
        exact_p = None
        # if insertVal < all vals, insert behind max value
        min_val = max_val = head.val 
        max_p = head 
        if head.val <= insertVal:
            exact_p = head 
        slow = head.next
        while slow != head:
            if slow.val <= insertVal:
                if not exact_p or exact_p.val <= slow.val:
                    exact_p = slow 
            # 
            min_val = min(min_val, slow.val)
            if slow.val >= max_val:
                max_val = slow.val 
                max_p = slow 
            # move to next 
            slow = slow.next 

        if insertVal > max_val or insertVal <= min_val:
            next_n = max_p.next 
            max_p.next = Node(insertVal, next_n)
        else:
            next_n = exact_p.next 
            exact_p.next = Node(insertVal, next_n)
        return head 










