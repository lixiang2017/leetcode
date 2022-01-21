'''

执行用时：64 ms, 在所有 Python3 提交中击败了98.23% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了30.68% 的用户
通过测试用例：8 / 8
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next 

    def getRandom(self) -> int:
        return choice(self.nums)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
