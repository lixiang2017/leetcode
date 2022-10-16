'''
DP, T: O(N), S: O(N)

执行用时：48 ms, 在所有 Python3 提交中击败了84.52%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了97.62%的用户
通过测试用例：109 / 109
'''
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        preCount, curAns, MOD = [0] * 26, 1, 10 ** 9 + 7
        for ch in s:
            newCount = curAns
            curAns = ((curAns + newCount) - preCount[ord(ch) - ord('a')]) % MOD
            preCount[ord(ch) - ord('a')] = newCount
        return curAns - 1

'''
https://leetcode.cn/problems/distinct-subsequences-ii/solution/bu-tong-by-capital-worker-vga3/
'''
