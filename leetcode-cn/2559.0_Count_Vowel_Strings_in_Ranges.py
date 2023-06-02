'''
执行用时：92 ms, 在所有 Python3 提交中击败了63.58% 的用户
内存消耗：46.7 MB, 在所有 Python3 提交中击败了58.94% 的用户
通过测试用例：93 / 93
'''
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        presum = [0]
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                presum.append(presum[-1] + 1)
            else:
                presum.append(presum[-1])
        return [presum[r + 1] - presum[l] for l, r in queries]

