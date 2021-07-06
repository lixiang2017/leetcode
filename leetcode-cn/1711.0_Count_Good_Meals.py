'''
63 / 70 个通过测试用例
状态：超出时间限制
提交时间：2 分钟内
'''
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        good = set(1 << i for i in range(22))
        deli = Counter(deliciousness)
        total = 0
        for d1, c1 in deli.items():
            for d2, c2 in deli.items():
                if d1 + d2 in good:
                    if d1 != d2:
                        total += c1 * c2
                    else:
                        total += c1 * (c1 - 1)

        return (total // 2) % MOD


'''
63 / 70 个通过测试用例
状态：超出时间限制
提交时间：2 分钟内
'''
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        good = set(1 << i for i in range(22))
        deli = Counter(deliciousness)
        deli2 = [(d, c) for d, c in deli.items()]
        N = len(deli2)
        total = 0        
        for i in range(N):
            for j in range(i, N):
                d1, c1 = deli2[i]
                d2, c2 = deli2[j]
                if d1 + d2 in good:
                    if d1 != d2:
                        total += c1 * c2
                    else:
                        total += c1 * (c1 - 1) // 2
                    total %= MOD

        return total


'''
Hash Table + Hash Set

执行用时：280 ms, 在所有 Python3 提交中击败了99.31% 的用户
内存消耗：20.4 MB, 在所有 Python3 提交中击败了69.45% 的用户
'''
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        good = set(1 << i for i in range(22))
        deli = Counter(deliciousness)
        total = 0
        for d1, c1 in deli.items():
            for g in good:
                if g - d1 in deli:
                    if d1 + d1 == g:
                        total += c1 * (c1 - 1)
                    else:
                        total += c1 * deli[g - d1]

        return (total // 2) % MOD
