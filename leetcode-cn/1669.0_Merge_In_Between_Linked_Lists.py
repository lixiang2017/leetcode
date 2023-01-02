'''
执行用时：380 ms, 在所有 Python3 提交中击败了61.70% 的用户
内存消耗：21.8 MB, 在所有 Python3 提交中击败了10.11% 的用户
通过测试用例：61 / 61
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy_a = ListNode(next=list1)
        ta1 = dummy_a 
        aa, bb = a, b 
        dist = b - a + 1
        while aa:
            ta1 = ta1.next 
            aa -= 1
        ta2 = ta1 
        while dist:
            ta2 = ta2.next 
            dist -= 1

        # find tail node of list2
        tb2 = list2 
        while tb2.next:
            tb2 = tb2.next 
        # link
        ta1.next = list2 
        tb2.next = ta2.next 
        return dummy_a.next 
        