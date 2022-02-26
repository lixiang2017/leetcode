'''
random

执行用时：3888 ms, 在所有 Python3 提交中击败了33.77% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了94.96% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        ans = 0
        for _ in range(3400):
            random.shuffle(nums)
            cur = 0
            cnt = Counter()
            for x in nums:
                j = 0
                for i in range(1, numSlots + 1):
                    if cnt[i] < 2 and (x & i) > (x & j):
                        j = i
                cnt[j] += 1
                cur += (x & j)
            ans = max(ans, cur)

        return ans 

