'''
Brute Force
Time: O(N^2)
Space: O(1)

72 / 89 个通过测试用例
状态：超出时间限制
提交时间：几秒前
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        N = len(nums)
        for end in range(N):
            total = 0
            for start in range(end, -1, -1):
                total += nums[start]
                if total == k:
                    count += 1

        return count




'''
# 1074. Number of Submatrices That Sum to Target
approach: Prefix Sum + Hash Table (Two Sum)
Time: O(N)
Space: O(N)

执行用时：116 ms, 在所有 Python3 提交中击败了17.33%的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了8.33%的用户
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = pre = 0
        N = len(nums)
        mp = defaultdict(int)
        mp[0] = 1

        for i in range(N):
            pre += nums[i]
            count += mp[pre - k]
            mp[pre] += 1

        return count


