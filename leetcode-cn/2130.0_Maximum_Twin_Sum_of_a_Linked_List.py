# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        n = len(values)
        return max(values[i] + values[n - 1 - i] for i in range(n//2))
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        ans = 0
        while head and head2:
            ans = max(ans, head.val + head2.val)
            head = head.next
            head2 = head2.next
        return ans

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre 
            pre = cur
            cur = nxt
        return pre 