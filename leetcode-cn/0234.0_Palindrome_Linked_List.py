'''
T: O(N), S:O(1)

执行用时：644 ms, 在所有 Python3 提交中击败了71.50% 的用户
内存消耗：40 MB, 在所有 Python3 提交中击败了85.30% 的用户
通过测试用例：86 / 86
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cnt = 0
        node = head 
        while node:
            cnt += 1
            node = node.next 
        
        half = cnt // 2
        if cnt % 2 == 0:
            half -= 1
        right_pre = head 
        while half:
            half -= 1
            right_pre = right_pre.next

        # cut 
        right_head = right_pre.next 
        right_pre.next = None 
        # reverse
        another = None
        while right_head:
            next_one = right_head.next 
            right_head.next = another
            another = right_head
            right_head = next_one
        
        # compare another list (right part list) and left part 
        while another and head:
            if another.val != head.val:
                return False 
            another, head = another.next, head.next 
        return True


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
    
    def middleNode(self, head: Optional[ListNode]) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
