'''
AC
'''
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        t = 0
        N = len(nums)
        seen = set()
        for i in range(N- 3):
            for j in range(i + 1, N - 2):
                for k in range(j + 1, N - 1):
                    for p in range(k + 1, N):
                        if nums[i] + nums[j] + nums[k] == nums[p] and (i, j, k, p) not in seen:
                            seen.add((i, j, k, p))
                            t += 1
        return t

    
'''
输入：[28,8,49,85,37,90,20,8]
输出：3
预期：1
'''


'''
211 / 211 个通过测试用例
状态：通过
执行用时: 1220 ms
内存消耗: 14.8 MB
提交时间：几秒前
'''
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        t = 0
        N = len(nums)
        seen = set()
        for i in range(N- 3):
            for j in range(i + 1, N - 2):
                for k in range(j + 1, N - 1):
                    for p in range(k + 1, N):
                        if nums[i] + nums[j] + nums[k] == nums[p]:
                            t += 1
        return t

