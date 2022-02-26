'''
approach: Hash Table
Time: O(N)
Space: O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了68.60%的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了24.33%的用户
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        return [num for num, cnt in freq.items() if cnt == 1][0]


'''
执行用时：40 ms, 在所有 Python3 提交中击败了60.54% 的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了5.25% 的用户
通过测试用例：14 / 14
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]


'''
检查每一位的贡献

执行用时：68 ms, 在所有 Python3 提交中击败了37.97% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了12.60% 的用户
通过测试用例：14 / 14
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(32):
            cnt = 0
            mask = (1 << i)
            for x in nums:
                if x & mask:
                    cnt += 1
            if cnt % 3:
                ans |= mask 
        # overflow
        if ans > (1 << 31) - 1:
            ans -= (1 << 32)
        return ans

