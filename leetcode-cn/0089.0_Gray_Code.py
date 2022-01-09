'''
straight + reverse

执行用时：44 ms, 在所有 Python3 提交中击败了71.61% 的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了25.27% 的用户
通过测试用例：16 / 16
'''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray = [0]
        for i in range(n):
            gray1 = [g + (1 << i) for g in gray[::-1]]
            gray += gray1 
        return gray 


'''
执行用时：32 ms, 在所有 Python3 提交中击败了98.28% 的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了78.06% 的用户
通过测试用例：16 / 16
'''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # G(i) = i ^ (i // 2)
        return [i ^ (i // 2) for i in range(1 << n)]
