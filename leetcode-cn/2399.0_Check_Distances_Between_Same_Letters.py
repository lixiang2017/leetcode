'''
执行用时：40 ms, 在所有 Python3 提交中击败了65.06% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了33.13% 的用户
通过测试用例：335 / 335
'''
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        indice = defaultdict(list)
        for i, ch in enumerate(s):
            indice[ch].append(i)
        for ch, (i, j) in indice.items():
            idx = ord(ch) - ord('a')
            if distance[idx] != j - i - 1:
                return False
        return True
        