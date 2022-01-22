'''
hash table
T: O(N)
S: O(N)

Runtime: 53 ms, faster than 51.57% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.7 MB, less than 9.97% of Python3 online submissions for Linked List Cycle II.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None




'''
math
T: O(N)
S: O(1)

# a b c, n圈
第一次遇见
slow: a + b
fast: a + n * (b + c) + b
=> 2 * (a + b) = a + n * (b + c) + b
=> a = c + (n - 1) * (b + c)
所以，让 slow2 重新从 head 出发，之前的 slow 从 遇见点 出发。两者每次都是走一步。
slow2 走 a 步到交点时，slow 转 (n - 1)圈，再走了 c 步，两者正好碰到。

Runtime: 90 ms, faster than 12.89% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.3 MB, less than 23.99% of Python3 online submissions for Linked List Cycle II.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow
        
        return None
