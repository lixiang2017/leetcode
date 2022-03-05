'''
recursion

执行用时：52 ms, 在所有 Python3 提交中击败了24.44% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了12.95% 的用户
通过测试用例：62 / 62
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if 1 == k:
            return head 
        # 1, 2,     3, 4, 5
        #    node
        cnt, node = 1, head 
        while node and node.next:
            node = node.next 
            cnt += 1
            if cnt >= k:
                break
        if cnt < k:
            return head 

        next_part = node.next
        # cut !!!
        node.next = None
        another = None
        first = head 
        # another_link_list -> ...
        # first/head -> second -> third -> ...
        while first:
            second = first.next 
            first.next = None
            # link to another, put it ahead
            first.next = another 
            another = first
            # move to next node 
            first = second 
        
        head.next = self.reverseKGroup(next_part, k)

        return another
