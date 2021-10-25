'''
monotonic stack
a decreasing stack
T: O(M + N)
S: O(N)

执行用时：24 ms, 在所有 Python3 提交中击败了98.75% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了12.42% 的用户
通过测试用例：15 / 15
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = dict()
        stack = []
        for x in nums2:
            while stack and stack[-1] < x:
                greater[stack.pop()] = x
            stack.append(x)
        return [greater[x] if x in greater else -1 for x in nums1]
