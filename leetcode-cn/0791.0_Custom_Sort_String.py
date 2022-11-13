'''
执行用时：36 ms, 在所有 Python3 提交中击败了72.50% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了16.50% 的用户
通过测试用例：39 / 39
'''
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ss = sorted(s, key = lambda ch: order.index(ch) if ch in order else -1)
        return ''.join(ss)



'''
hash table

执行用时：44 ms, 在所有 Python3 提交中击败了22.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了49.50% 的用户
通过测试用例：39 / 39
'''
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        c = Counter(s)
        order_set = set(order)
        return ''.join(ch * c[ch] for ch in order) + \
            ''.join(ch * cnt for ch, cnt in c.items() if ch not in order_set)

'''
执行用时：36 ms, 在所有 Python3 提交中击败了72.50% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了69.00% 的用户
通过测试用例：39 / 39
'''
 class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return ''.join(sorted(s, key=lambda ch: order.find(ch)))
