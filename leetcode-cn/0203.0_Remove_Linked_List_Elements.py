'''
Three Pointers,T:O(N),S:O(1)

执行用时：96 ms, 在所有 Python3 提交中击败了5.07% 的用户
内存消耗：17.8 MB, 在所有 Python3 提交中击败了75.49% 的用户
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = prev = post = ListNode(next=head)
        while post and post.next:
            if post.next.val == val:
                post = post.next
            else:
                prev.next = post.next
                post = post.next
                prev = post
        prev.next = None
        return dummy.next


'''
DFS,T:O(N),S:O(N)

执行用时：76 ms, 在所有 Python3 提交中击败了44.93% 的用户
内存消耗：28.2 MB, 在所有 Python3 提交中击败了5.02% 的用户
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        def dfs(prev, post, val):
            if not post:
                return 
            if post.val == val:
                prev.next = post.next
            else:
                prev = post
            dfs(prev, prev.next, val)

        dfs(dummy, dummy.next, val)
        return dummy.next
