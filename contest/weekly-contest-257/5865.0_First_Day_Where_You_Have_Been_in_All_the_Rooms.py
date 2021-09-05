'''
总结：
1、题目要看清。比赛的时候0 <= nextVisit[i] <= i这个条件没看到。无形之中给自己加大了难度。
2、多举几个例子，手动模拟。找规律。
3、有点高中数学归纳法的意思。


// 假如nextVisit = [0, 0, 0, 0]
// 要走到1号房，要经过 0 0
// 要走到2号房，要经过 0 0 1 0 0 1
// 要走到3号房，要经过 0 0 1 0 0 1 2 0 0 1 0 0 1 2
// 明显得 dp[i] = dp[i - 1] * 2 + 2

// 假如nextVisit = [0, 1, 0, 2, 4, 4]
// 要走到1号房，要经过 0 0
// 要走到2号房，要经过 0 0 1 1
// 要走到3号房，要经过 0 0 1 1 2 0 0 1 1 2
// 要走到4号房，要经过 0 0 1 1 2 0 0 1 1 2 3 2 0 0 1 1 2 3
// 要走到5号房，要经过 0 0 1 1 2 0 0 1 1 2 3 2 0 0 1 1 2 3 4 4
// 与nextVisit[i]全为0对比，nextVisit[i]让我们跳过从0到nextVisit[i]这段要经过的路径
// 比如要走到2号房，0 0 1 (0 0) 1，括号内的就是nextVisit[i]跳过的路径
// 所以有 dp[i] = dp[i - 1] * 2 + 2 - dp[nextVisit[i - 1]]



执行用时：232 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：25.9 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：239 / 239
'''
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        N = len(nextVisit)
        MOD = 10 ** 9 + 7
        dp = [0] * N
        for i in range(1, N):
            dp[i] = (2 * dp[i - 1] + 2 - dp[nextVisit[i - 1]]) % MOD
        return dp[-1]
