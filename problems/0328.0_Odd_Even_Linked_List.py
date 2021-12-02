'''
T: O(N)
S: O(1)

Runtime: 48 ms, faster than 40.20% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 16.4 MB, less than 14.50% of Python3 online submissions for Odd Even Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyOdd = node1 = ListNode()
        dummyEven = node2 = ListNode()
        node, idx = head, 0
        while node:
            idx += 1
            if idx & 1:
                node1.next = node
                node1 = node1.next
                # node1.next = None
            else:
                node2.next = node
                node2 = node2.next
                # node2.next = None
            node = node.next
        # link
        node1.next = dummyEven.next
        node2.next = None
        
        return dummyOdd.next
        
