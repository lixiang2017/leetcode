'''
python3

ref:
https://leetcode-cn.com/problems/count-sorted-vowel-strings/solution/tong-ji-zi-dian-xu-yuan-yin-zi-fu-chuan-de-shu-mu-/
https://leetcode-cn.com/problems/count-sorted-vowel-strings/solution/ke-zhong-zu-he-wen-ti-by-amazingt-18v7/


You are here!
Your runtime beats 87.83 % of python3 submissions.
You are here!
Your memory usage beats 80.97 % of python3 submissions.
'''

import math

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n + 5 - 1, 4)   
    