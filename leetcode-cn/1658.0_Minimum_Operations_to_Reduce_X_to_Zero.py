'''
sliding window + 补集思想
T: O(N)
S: O(1)

执行用时：236 ms, 在所有 Python3 提交中击败了61.16% 的用户
内存消耗：25.2 MB, 在所有 Python3 提交中击败了73.66% 的用户
通过测试用例：94 / 94
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n, s = len(nums), sum(nums)
        # may cause `need` is a negative number
        if s < x:
            return -1
        need = s - x 
        ans = inf 
        i, j = 0, 0
        t = 0
        while t < need and j < n:
            t += nums[j]
            j += 1
        # from 0 to j-1 is j, use n - j
        if t == need:
            ans = min(ans, n - j)

        while i < n:
            t -= nums[i]
            while t < need and j < n:
                t += nums[j]
                j += 1
            # from i+1 to j-1, j-1-(i+1)+1 = j - i - 1; so n - this
            if t == need:
                ans = min(ans, n - (j - i - 1))
            # prunning
            if t < need and j == n:
                break
            i += 1

        return ans if ans != inf else -1

