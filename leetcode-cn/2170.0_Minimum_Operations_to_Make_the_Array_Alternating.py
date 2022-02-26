'''
1、出现少于两种数字的，补零即可；
2、分情况讨论。
2.1 频率最高的两个数，只要两个数不相同，相加即可。
2.2 此外，top2数字均一样，取交叉和大者；top1数字一样，取交叉和大者。 所以，这种情况取交叉和大的即可。


执行用时：316 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：33.8 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：127 / 127
'''
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        even, odd = Counter(nums[:: 2]), Counter(nums[1:: 2])
        evens = sorted([(c, x) for x, c in even.items()], reverse=True)
        odds = sorted([(c, x) for x, c in odd.items()], reverse=True)
        top2even = evens[: 2]
        top2odd = odds[: 2]
        top2even += (2 - len(top2even)) * [(0, 0)]
        top2odd += (2 - len(top2odd)) * [(0, 0)]
        if top2even[0][1] != top2odd[0][1]:
            return n - (top2even[0][0] + top2odd[0][0])
        else:
            return n - max(top2even[0][0] + top2odd[1][0], top2even[1][0] + top2odd[0][0])

