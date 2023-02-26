'''
hash table

执行用时：32 ms, 在所有 Python3 提交中击败了90.97% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # diff pairs count, (x, y) (y, x)
        diff = Counter()
        for a, b in zip(s1, s2):
            if a != b:
                diff[(a, b)] += 1
        xy = diff[('x', 'y')]
        yx = diff[('y', 'x')]
        if xy & 1 and yx & 1:
            return 2 + (xy // 2) + (yx // 2)
        elif not (xy & 1) and not (yx & 1):
            return (xy // 2) + (yx // 2)
        else:
            return -1

'''
执行用时：36 ms, 在所有 Python3 提交中击败了75.69% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
        if (xy + yx) & 1:
            return -1
        return xy // 2 + yx // 2 + xy % 2 + yx % 2
        
        