'''
hash set + while 
T: O(M + N)
S: O(N)

执行用时：80 ms, 在所有 Python3 提交中击败了64.71% 的用户
内存消耗：20.4 MB, 在所有 Python3 提交中击败了56.21% 的用户
通过测试用例：57 / 57
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        while nums and head:
            if head.val in nums:
                while head and head.val in nums:
                    nums.remove(head.val)
                    head = head.next 
                ans += 1

            if head:
                head = head.next 

        return ans 
