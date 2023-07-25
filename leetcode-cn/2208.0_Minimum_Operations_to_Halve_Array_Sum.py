'''
heap

执行用时：348 ms, 在所有 Python3 提交中击败了80.00% 的用户
内存消耗：30.7 MB, 在所有 Python3 提交中击败了10.00% 的用户
通过测试用例：62 / 62
'''
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s, op, reduced = sum(nums), 0, 0
        h = [-x for x in nums]
        heapify(h)
        while reduced < s / 2:
            op += 1
            x = -h[0]
            reduced += x / 2
            heapreplace(h, h[0] / 2)
        return op

'''
执行用时：408 ms, 在所有 Python3 提交中击败了40.00% 的用户
内存消耗：29.7 MB, 在所有 Python3 提交中击败了58.00% 的用户
通过测试用例：62 / 62
'''
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s, op, reduced = sum(nums), 0, 0
        h = [-x for x in nums]
        heapify(h)
        while reduced < s / 2:
            op += 1
            reduced += -h[0] / 2
            heapreplace(h, h[0] / 2)
        return op

'''
执行用时：332 ms, 在所有 Python3 提交中击败了88.00% 的用户
内存消耗：30.6 MB, 在所有 Python3 提交中击败了30.00% 的用户
通过测试用例：62 / 62
'''
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s, op, reduced = sum(nums), 0, 0
        h = [-x for x in nums]
        heapify(h)
        while reduced < s / 2:
            op += 1
            reduced -= h[0] / 2
            heapreplace(h, h[0] / 2)
        return op

