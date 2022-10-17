'''
T： O（N）
S： O（1）

Runtime: 49 ms, faster than 81.85% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 14.3 MB, less than 15.04% of Python3 online submissions for Delete Node in a Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node and node.next:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
                break
            node = node.next


'''
T： O（1）
S： O（1）

Runtime: 84 ms, faster than 21.30% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 14.1 MB, less than 91.10% of Python3 online submissions for Delete Node in a Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next 
        node.val = nextNode.val 
        node.next = nextNode.next 
        del nextNode
