'''
正向处理
T: O(log(target))
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了32.43% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了90.09% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # double count
        d = 0
        while startValue < target:
            d += 1
            startValue *= 2
        # 多翻倍了，要一点一点赔偿回去。但是最多只能有d步可移动。
        diff = startValue - target
        ans = d 
        while diff and d:
            if diff & 1:
                ans += 1
            diff >>= 1
            d -= 1
        # 没有多余的移位可用了，只能 -1 -1 -1，一步步减
        ans += diff
        return ans 
