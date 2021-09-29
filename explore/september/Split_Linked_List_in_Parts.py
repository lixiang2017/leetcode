'''
T: O(2N)
S: O(k)

You are here!
Your runtime beats 65.79 % of python3 submissions.
You are here!
Your memory usage beats 73.86 % of python3 submissions.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def getLen(node):
            c = 0
            while node:
                c += 1
                node = node.next
            return c
        
        N = getLen(head)
        ans = []
        avg, remain = divmod(N, k)
        node = pre = head
        while node:
            ans.append(node)
            k -= 1
            for _ in range(avg):
                pre = node
                node = node.next
            if remain:
                pre = node
                node = node.next
                remain -= 1
            pre.next = None
        
        return ans + [None] * k
