'''
AC
Brute Force
T: O(N^2)
S: O(1)
'''
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans, N = 0, len(nums)
        for i in range(N - 1):
            for j in range(i + 1, N):
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans

'''
Hash Table
T: O(N)
S: O(N)

执行用时：40 ms, 在所有 Python3 提交中击败了91.35% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了45.83% 的用户
通过测试用例：236 / 236
'''
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans, c = 0, Counter(nums)
        for x, cnt in c.items():
            ans += cnt * c[x + k]
        return ans
