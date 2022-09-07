'''
计算贡献
T： O（2N）
S： O（N）

执行用时：312 ms, 在所有 Python3 提交中击败了56.92% 的用户
内存消耗：19.8 MB, 在所有 Python3 提交中击败了49.47% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        indice = defaultdict(list)
        for i, ch in enumerate(s):
            if 0 == len(indice[ch]):
                indice[ch].append(-1)
            indice[ch].append(i)
        for ch in indice:
            if len(indice[ch]) > 1:
                indice[ch].append(n)

        ans = 0
        for ch, positions in indice.items():
            if len(positions) > 2:
                pl = len(positions)
                for i in range(1, pl - 1):
                    ans += (positions[i] - positions[i - 1]) * (positions[i + 1] - positions[i])
        return ans 
