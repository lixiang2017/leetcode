'''
Two Pointers, fast and slow
T: O(N)
S: O(1)

Runtime: 32 ms, faster than 60.47% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.2 MB, less than 46.38% of Python3 online submissions for Middle of the Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

'''
output to array
T: O(N)
S: O(N)

Runtime: 32 ms, faster than 60.47% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.3 MB, less than 11.11% of Python3 online submissions for Middle of the Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]

'''
Two Pointers, fast and slow
T: O(N)
S: O(1)

Runtime: 59 ms, faster than 40.14% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.9 MB, less than 55.96% of Python3 online submissions for Middle of the Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = ListNode(next=head)
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return slow

