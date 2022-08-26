'''
执行用时：36 ms, 在所有 Python3 提交中击败了69.76% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了51.40% 的用户
通过测试用例：104 / 104
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        h = [-x for x in nums]
        heapify(h)
        x1, x2 = -heappop(h), -heappop(h)
        return (x1 - 1) * (x2 - 1)

'''
执行用时：36 ms, 在所有 Python3 提交中击败了69.76% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了49.03% 的用户
通过测试用例：104 / 104
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        h = [-x for x in nums]
        heapify(h)
        x1, x2 = nsmallest(2, h)
        return (-x1 - 1) * (-x2 - 1)


'''
执行用时：48 ms, 在所有 Python3 提交中击败了19.52% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了69.52% 的用户
通过测试用例：104 / 104
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums1 = list(map(lambda x: x - 1, nums))
        nums1.sort()
        return max(nums1[0] * nums1[1], nums1[-1] * nums1[-2])
