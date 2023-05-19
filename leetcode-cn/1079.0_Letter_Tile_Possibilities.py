'''
执行用时：72 ms, 在所有 Python3 提交中击败了65.69% 的用户
内存消耗：17.9 MB, 在所有 Python3 提交中击败了25.55% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        possibilities = set()
        n = len(tiles)
        for mask in range(1, 1 << n):
            s = ''.join(tiles[i] for i in range(n) if mask >> i & 1)
            possibilities.update(permutations(s))
        return len(possibilities)
