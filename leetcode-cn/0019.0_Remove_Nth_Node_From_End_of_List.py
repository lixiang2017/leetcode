'''
执行用时：20 ms, 在所有 Python3 提交中击败了99.71% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了56.14% 的用户
通过测试用例：208 / 208
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        p1 = p2 = dummy
        n += 1
        while n:
            p1 = p1.next
            n -= 1
        while p1:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next
        
        return dummy.next


'''
执行用时：36 ms, 在所有 Python3 提交中击败了79.64% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了35.81% 的用户
通过测试用例：208 / 208
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = q = head 
        for _ in range(n):
            p = p.next 
        if p is None:
            return head.next 
        while p.next:
            p = p.next 
            q = q.next 
        q.next = q.next.next 

        return head 



