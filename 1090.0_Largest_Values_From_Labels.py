'''
sort + hash table

执行用时：68 ms, 在所有 Python3 提交中击败了36.84% 的用户
内存消耗：21.1 MB, 在所有 Python3 提交中击败了6.32% 的用户
通过测试用例：81 / 81
'''
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        pairs = list(zip(values, labels))
        pairs.sort(reverse=True)
        label_cnt = Counter()
        ans = 0
        for value, label in pairs:
            if label_cnt[label] < useLimit:
                ans += value 
                label_cnt[label] += 1
                numWanted -= 1
                if numWanted == 0:
                    break
        return ans 
