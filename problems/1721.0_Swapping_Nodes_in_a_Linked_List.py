'''
two passes
just swap values, k_th and n-k+1_th
T: O(2N)
S: O(1)

Runtime: 1540 ms, faster than 35.46% of Python3 online submissions for Swapping Nodes in a Linked List.
Memory Usage: 48.6 MB, less than 31.04% of Python3 online submissions for Swapping Nodes in a Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node, n = head, 0
        while node:
            n += 1
            node = node.next

        if k > n - k + 1:
            k = n - k + 1
        elif n % 2 and k == (n + 1) // 2:
            return head

        ptr1 = ptr2 = None
        idx, node = 1, head        
        while node:
            if idx == k:
                ptr1 = node
            if idx == n - k + 1:
                ptr2 = node
                break
            node = node.next
            idx += 1
        ptr1.val, ptr2.val = ptr2.val, ptr1.val
        return head 


'''
only one pass

ref:
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1009800/C%2B%2BJP3-One-Pass

Runtime: 1056 ms, faster than 95.98% of Python3 online submissions for Swapping Nodes in a Linked List.
Memory Usage: 48.4 MB, less than 85.24% of Python3 online submissions for Swapping Nodes in a Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        n1 = n2 = None
        while p:
            k -= 1
            if n2:
                n2 = n2.next
            if k == 0:
                n1 = p
                n2 = head     
            p = p.next 
        n1.val, n2.val = n2.val, n1.val
        return head 
        
'''
Runtime: 1043 ms, faster than 37.74% of Python3 online submissions for Swapping Nodes in a Linked List.
Memory Usage: 50.7 MB, less than 22.68% of Python3 online submissions for Swapping Nodes in a Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total, node = 0, head
        while node:
            total += 1
            node = node.next
        p = q = None
        i = 0
        node = head
        while i < k or i < total - k + 1:
            i += 1
            if i == k:
                p = node
            if i == total - k + 1:
                q = node
            node = node.next
        p.val, q.val = q.val, p.val
        return head
        
