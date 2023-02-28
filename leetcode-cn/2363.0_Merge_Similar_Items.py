'''
hash table, using array, no sort

执行用时：40 ms, 在所有 Python3 提交中击败了85.45% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了42.91% 的用户
通过测试用例：49 / 49
'''
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # value -> weight
        weights = [0] * 1001
        for value, weight in chain(items1, items2):
            weights[value] += weight
        return [[v, weights[v]] for v in range(1001) if weights[v] != 0]
        
