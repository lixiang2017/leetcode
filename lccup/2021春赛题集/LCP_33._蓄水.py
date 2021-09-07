'''
ref:
https://leetcode-cn.com/problems/o8SXZn/solution/c-python3-mo-ni-yi-qing-dao-ci-shu-wei-z-lcfx/

执行用时：108 ms, 在所有 Python3 提交中击败了85.71% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了42.86% 的用户
通过测试用例：37 / 37
'''
class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        maxvat = max(vat)
        if maxvat == 0:
            return 0

        min_pour = 1
        max_pour = maxvat
        ans = float('inf')
        N = len(vat)
        # to upgrade
        for pour_time in range(min_pour, max_pour + 1):
            if pour_time >= ans:
                break
            cur = pour_time
            for i in range(N):
                need_bucket_size = ceil(vat[i] / pour_time)
                cur += max(0, need_bucket_size - bucket[i])
            ans = min(ans, cur)

        return ans
