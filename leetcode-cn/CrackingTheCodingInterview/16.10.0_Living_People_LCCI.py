'''
差分数组
T: O(4N)
S: O(N)

执行用时：52 ms, 在所有 Python3 提交中击败了92.56% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了76.74% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        # 1900-2000 -> 0-100
        diff = [0] * 102
        for b in birth:
            diff[b - 1900] += 1
        for d in death:
            diff[d - 1900 + 1] -= 1
        m = year = 0
        for i, p in enumerate(accumulate(diff)):
            if p > m:
                m = p
                year = i
        return 1900 + year
