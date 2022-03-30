'''
DFS

执行用时：52 ms, 在所有 Python3 提交中击败了99.44% 的用户
内存消耗：21.1 MB, 在所有 Python3 提交中击败了7.93% 的用户
通过测试用例：32 / 32
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
        nums = []
        while head:
            nums.append(head.val)
            head = head.next 

        def convert(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = convert(l, mid - 1)
            node.right = convert(mid + 1, r)
            return node 
        
        return convert(0, len(nums) - 1)

'''
DFS, 直接切分列表，不用转化成数组

执行用时：56 ms, 在所有 Python3 提交中击败了96.04% 的用户
内存消耗：18.4 MB, 在所有 Python3 提交中击败了87.00% 的用户
通过测试用例：32 / 32
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
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)
        
        pre, p, q = head, head.next, head.next.next 
        # to find mid 
        while q and q.next:
            pre = pre.next 
            p = p.next 
            q = q.next.next 
        # to cut 
        pre.next = None 
        node = TreeNode(p.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(p.next)
        return node 



