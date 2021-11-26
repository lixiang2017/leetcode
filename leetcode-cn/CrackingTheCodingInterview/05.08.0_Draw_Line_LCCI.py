'''
执行用时：32 ms, 在所有 Python3 提交中击败了83.33% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了64.58% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        ans = [0] * length
        height = length * 32 // w
        one_row_cnt = w // 32
        idx0 = one_row_cnt * y
        more1, bits1 = divmod(x1, 32)
        more2, bits2 = divmod(x2, 32)
        idx1 = idx0 + more1
        if bits1 == 0:
            ans[idx1] = -1
        else:
            ans[idx1] += (1 << (32 - bits1)) - 1
        if idx1 < idx0 + more2:
            idx1 += 1
            while idx1 < idx0 + more2:
                ans[idx1] = -1
                idx1 += 1
        ans[idx1] += (1 << (32)) - 1
        ans[idx1] -= (1 << (32 - 1 - bits2)) - 1
        if ans[idx1] > (1 << (32)) - 1:
            ans[idx1] -= (1 << (32)) - 1
        else:
            # ans[idx1] = -1  # wrong
            # negative, to remove left most 1, ~ and +1
            ans[idx1] &= (1 << 31) - 1
            ans[idx1] -= 2147483648
        return ans

'''
输入：
2
64
0
52
0
输出：
[-1,-1]
预期结果：
[-1,-2048]
'''
