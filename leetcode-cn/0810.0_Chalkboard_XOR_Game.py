'''
approch: Math
Time: O(N)
Space: O(1)

执行用时：88 ms, 在所有 Python3 提交中击败了60.61% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了96.97% 的用户
'''

from operator import xor
from itertools import accumulate
from functools import reduce

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return (0 == (len(nums) & 1)) or (reduce(xor, nums) == 0)


'''
# 补充：博弈论/游戏论/对策论/Game Theory
ICG/公共组合游戏/Impartial Combinational Games
https://www.bilibili.com/video/av48199226
https://zhuanlan.zhihu.com/p/161031067

囚徒困境
巴什博弈（Bash Game）
斐波那契博弈（Fibonacci Nim Game）
威佐夫博弈（Wythoff Game）
尼姆博弈（Nimm Game）
SG函数
SG定理
'''