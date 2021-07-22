'''
Hash Set
执行用时：28 ms, 在所有 Python3 提交中击败了98.20% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了79.35% 的用户
'''
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cover = set()
        for r in ranges:
            for num in range(r[0], r[1] + 1):
                cover.add(num)
        for n in range(left, right + 1):
            if n not in cover:
                return False
        return True
