'''
约瑟夫环，等差数列求最后剩余的首项
T: O(logN)
S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了35.07% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了87.31% 的用户
通过测试用例：3377 / 3377
'''
class Solution:
    def lastRemaining(self, n: int) -> int:
        a1 = 1
        k, cnt, step = 0, n, 1
        while cnt > 1:
            if k % 2 == 0: # 正向
                a1 += step
            else: # 反向
                # 还剩余偶数个： 首项不变
                # 还剩余奇数个： 首项+step
                if cnt % 2:
                    a1 += step 
            k += 1
            cnt >>= 1
            step <<= 1

        return a1 
