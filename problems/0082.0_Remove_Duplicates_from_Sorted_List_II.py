'''
T: O(3*N + NlogN)
S: O(2*N)

Runtime: 67 ms, faster than 33.87% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 14 MB, less than 54.61% of Python3 online submissions for Remove Duplicates from Sorted List II.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        c = Counter()
        while node:
            c[node.val] += 1
            node = node.next
        
        once = [v for v, cnt in c.items() if 1 == cnt]
        once.sort()
        hair = node = ListNode()
        for v in once:
            node.next = ListNode(val = v)
            node = node.next
        
        return hair.next
            

'''
Sentinel Head + Predecessor
T: O(N)
S: O(1)

Runtime: 68 ms, faster than 31.98% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 13.9 MB, less than 54.61% of Python3 online submissions for Remove Duplicates from Sorted List II.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sentinel
        sentinel = ListNode(0, head)
        # predecessor = the last node
        # before the sublist of duplicates
        pred = sentinel
        
        while head:
            # if it's a beginning of duplicates sublist
            # skip all duplicates
            if head.next and head.next.val == head.val:
                # move till the end of duplicates sublist
                while head.next and head.next.val == head.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next
            # otherwise, move predecessor
            else:
                pred = pred.next
            # move forward
            head = head.next 
            
        return sentinel.next
    

