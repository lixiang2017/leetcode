'''
sliding window

执行用时：84 ms, 在所有 Python3 提交中击败了 66.45% 的用户
内存消耗：29.9 MB, 在所有 Python3 提交中击败了9.21%的用户
通过测试用例：118 / 118
'''
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i, n = 0, len(arr)
        while i < n - 1 and arr[i] <= arr[i + 1]:
            i += 1
        if i == n - 1:
            return 0
        r = n - 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1

        ans = min(n - i - 1, r)
        j = n - 1
        while i >= 0:
            while j >= r and arr[j] >= arr[i]:
                j -= 1
            ans = min(ans, j - i)
            i -= 1
        ans = min(ans, j)
        return ans 


'''
通过测试用例：
105 / 118
输入：
[16,10,0,3,22,1,14,7,1,12,15]
输出：
10
预期结果：
8
'''
