'''
approach: Dynamic Programming
Time: O(N ^ 2 + N) = (N ^ 2)
Space: O(N)

执行用时：2896 ms, 在所有 Python 提交中击败了9.63%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了46.38%的用户
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        N = len(nums)
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


'''
approach: Greedy + Binary Search
Time: O(NlogN)
Space: O(N)

执行用时：40 ms, 在所有 Python 提交中击败了90.65%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了96.49%的用户
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = []
        for num in nums:
            if not d or num > d[-1]:
                d.append(num)
            else:
                left, right = 0, len(d) - 1
                loc = right
                while left <= right:
                    mid = (left + right) / 2
                    if d[mid] >= num:
                        loc = mid
                        right = mid - 1
                    else:
                        left = mid + 1

                d[loc] = num
        return len(d)


'''
Greedy+BinarySearch,T:O(NlogN),S:O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了99.69% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.79% 的用户
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if not dp or dp[-1] < num:
                dp.append(num)
            else:
                dp[bisect.bisect_left(dp, num)] = num
        return len(dp)


'''
remove ``not q``
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        q = []
        for n in nums:
            idx = bisect_left(q, n)
            if idx == len(q):
                q.append(n)
            else:
                q[idx] = n
        return len(q)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1

        return max(dfs(i) for i in range(n))
    
    
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j])
            f[i] += 1
        return max(f)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []
        for x in nums:
            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
        return len(g)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ng = 0
        for x in nums:
            j = bisect_left(nums, x, 0, ng)
            nums[j] = x
            if j == ng:                
                ng += 1
        return ng