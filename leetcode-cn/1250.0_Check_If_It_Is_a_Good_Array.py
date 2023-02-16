'''
number theory

ax+by=1 has solution x, y if gcd(a,b) = 1.
裴蜀定理
Bézout's lemma

https://baike.baidu.com/item/%E8%A3%B4%E8%9C%80%E5%AE%9A%E7%90%86/5186593


执行用时：48 ms, 在所有 Python3 提交中击败了78.43% 的用户
内存消耗：22.4 MB, 在所有 Python3 提交中击败了74.51% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1

'''
执行用时：56 ms, 在所有 Python3 提交中击败了56.86% 的用户
内存消耗：22 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return gcd(*nums) == 1
