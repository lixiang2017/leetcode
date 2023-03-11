'''
DFS

Runtime: 136 ms, faster than 26.88% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 20.4 MB, less than 10.50% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        def construct(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            if l == r:
                return TreeNode(vals[l])
            mid = (l + r) // 2
            return TreeNode(vals[mid], construct(l, mid - 1), construct(mid + 1, r))
        
        return construct(0, len(vals) - 1)
        

'''
DFS
no need to use if l == r:

Runtime: 119 ms, faster than 88.17% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 20.3 MB, less than 26.39% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        def construct(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) // 2
            return TreeNode(vals[mid], construct(l, mid - 1), construct(mid + 1, r))
        
        return construct(0, len(vals) - 1)
        
