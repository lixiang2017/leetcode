'''
sliding window + hash table, T: O(N), S: O(1)

执行用时：440 ms, 在所有 Python3 提交中击败了31.32% 的用户
内存消耗：20.4 MB, 在所有 Python3 提交中击败了40.01% 的用户
通过测试用例：91 / 91
'''
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        b = Counter()
        ans = j = 0
        for i, f in enumerate(fruits):
            b[f] += 1
            while len(b) > 2:
                b[fruits[j]] -= 1
                if b[fruits[j]] == 0:
                    b.pop(fruits[j])
                j += 1
            ans = max(ans, i - j + 1)
        return ans 
