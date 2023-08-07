'''
recursion
T: O(N)
S: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了52.82% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了12.24% 的用户
通过测试用例：55 / 55
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head 

        dummy = ListNode(next=head)
        next_head = head.next.next
        head.next.next = None 
        next_part = self.swapPairs(next_head)
        first, second = head, head.next 
        head.next = None
        dummy.next, first.next, second.next = second, next_part, first

        return dummy.next


'''
recursion

执行用时：36 ms, 在所有 Python3 提交中击败了52.82% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了43.33% 的用户
通过测试用例：55 / 55
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head 

        dummy = ListNode(next=head)
        next_part = self.swapPairs(head.next.next)
        first, second = head, head.next 
        dummy.next, first.next, second.next = second, next_part, first
        return dummy.next

'''
执行用时：36 ms, 在所有 Python3 提交中击败了52.82% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了50.24% 的用户
通过测试用例：55 / 55
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head 

        new_head = head.next
        head.next = self.swapPairs(head.next.next)
        new_head.next = head 
        return new_head 


'''
iteration

执行用时：36 ms, 在所有 Python3 提交中击败了52.82% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了80.98% 的用户
通过测试用例：55 / 55
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        cur = dummy 
        while cur.next and cur.next.next:
            # cur/dummy -> first/head -> second -> ...
            first, second = cur.next, cur.next.next 
            # change pointer
            # cur -> second -> first -> ...
            cur.next, second.next, first.next = second, first, second.next  
            # move to next part
            cur = cur.next.next 

        return dummy.next 


'''
iteration, 拆分出所有步骤

执行用时：32 ms, 在所有 Python3 提交中击败了77.26% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了62.82% 的用户
通过测试用例：55 / 55
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        cur = dummy 
        while cur.next and cur.next.next:
            # cur/dummy -> first/head -> second -> next_part
            first, second  = cur.next, cur.next.next
            next_part = second.next 
            # change pointer
            # cur -> second -> first -> next_part
            ## set to None
            cur.next = None
            first.next = None
            second.next = None 
            ## change
            cur.next = second
            second.next = first
            first.next = next_part 
            # move to next part
            cur = first 

        return dummy.next 


'''
执行用时：28 ms, 在所有 Python3 提交中击败了98.89% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了27.38% 的用户
通过测试用例：55 / 55
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        cur = head
        while cur:
            if cur.next:
                next_part = cur.next.next 
                one, two = cur, cur.next 
                # cut
                one.next, two.next = None, None 
                # link
                node.next = two
                two.next = one 
                # move 
                node = one  
                cur = next_part 
            else:
                node.next = cur 
                break

        return dummy.next 
