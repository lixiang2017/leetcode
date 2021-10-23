'''
math

执行用时：1256 ms, 在所有 Python3 提交中击败了12.70% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了96.56% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for L in range(int(sqrt(area)), area + 1):
            W = area // L
            if L * W == area and L >= W:
                return [L, W]

'''
输入：
2
输出：
[1,2]
预期结果：
[2,1]
'''
