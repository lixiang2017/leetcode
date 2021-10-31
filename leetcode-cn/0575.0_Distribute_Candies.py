'''
Hash Table

执行用时：84 ms, 在所有 Python3 提交中击败了67.68% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了87.31% 的用户
通过测试用例：206 / 206
'''
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(Counter(candyType)))


'''
Hash Set

执行用时：84 ms, 在所有 Python3 提交中击败了67.68% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了52.82% 的用户
通过测试用例：206 / 206
'''
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))
