'''
ref:
https://leetcode-cn.com/problems/stone-game-ix/solution/pythonpan-duan-aliceneng-fou-huo-sheng-b-unyt/

执行用时：140 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：25 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：93 / 93
'''
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0] * 3
        for v in stones:
            cnt[v % 3] += 1
        if cnt[0] % 2 == 0 and cnt[1] * cnt[2] > 0:
            return True
        if cnt[0] % 2 == 1 and abs(cnt[1] - cnt[2]) >= 3:
            return True
        return False

'''
执行用时：148 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：24.6 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：93 / 93
'''
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = Counter(v % 3 for v in stones)
        return abs(cnt[1] - cnt[2]) > 2 if cnt[0] & 1 else cnt[1] * cnt[2] > 0

