'''
hash table

执行用时：72 ms, 在所有 Python3 提交中击败了57.87% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了74.07% 的用户
通过测试用例：219 / 219
'''
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter(x for x in nums if x % 2 == 0)
        ans = -1
        for x, cnt in c.items():
            if ans == -1 or c[ans] < cnt or (c[ans] == cnt and x < ans):
                ans = x
        return ans 
