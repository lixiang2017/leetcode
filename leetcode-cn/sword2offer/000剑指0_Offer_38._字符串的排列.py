'''
执行用时：124 ms, 在所有 Python3 提交中击败了70.91% 的用户
内存消耗：23.2 MB, 在所有 Python3 提交中击败了14.41% 的用户
'''

from itertools import permutations
class Solution:
    def permutation(self, s: str) -> List[str]:
        return list(set([''.join(p) for p in list(permutations(s, len(s)))]))

'''
输入：
"aab"
输出：
["aab","aba","aab","aba","baa","baa"]
预期结果：
["aba","aab","baa"]
'''

