'''
two pointers

执行用时：116 ms, 在所有 Python3 提交中击败了71.34% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了6.37% 的用户
通过测试用例：64 / 64
'''
class Solution:
    def magicalString(self, n: int) -> int:
        magical = [1, 2, 2]
        i = 2
        while len(magical) < n:
            if magical[-1] == 2:
                magical += [1] * magical[i]
            else:
                magical += [2] * magical[i]
            i += 1
        return Counter(magical[: n])[1]

'''
执行用时：136 ms, 在所有 Python3 提交中击败了53.50% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了26.12% 的用户
通过测试用例：64 / 64
'''
class Solution:
    def magicalString(self, n: int) -> int:
        magical = [1, 2, 2]
        i = 2
        while len(magical) < n:
            if magical[-1] == 2:
                magical += [1] * magical[i]
            else:
                magical += [2] * magical[i]
            i += 1
        return sum(magical[i] == 1 for i in range(n))

