'''
执行用时：36 ms, 在所有 Python3 提交中击败了70.50% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.04% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -inf
        for w in s.split():
            if w.isdigit():
                x = int(w)
                if prev >= x:
                    return False
                prev = x 
        return True

'''
执行用时：36 ms, 在所有 Python3 提交中击败了70.50% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了8.63% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -inf
        for w in filter(str.isdigit, s.split()):
            x = int(w)
            if prev >= x:
                return False
            prev = x 
        return True

'''
执行用时：36 ms, 在所有 Python3 提交中击败了70.50% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了15.11% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(w) for w in s.split() if w.isdigit()]
        return sorted(nums) == nums and len(set(nums)) == len(nums)

'''
执行用时：40 ms, 在所有 Python3 提交中击败了45.32% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.04% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = list(map(int, filter(str.isdigit, s.split())))
        return sorted(nums) == nums and len(set(nums)) == len(nums)
                  