'''
simulation, T: O(N), S:O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了63.56% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了87.84% 的用户
通过测试用例：111 / 111
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, digits[-1] = divmod(digits[-1] + 1, 10)
        N = len(digits)
        i = N - 2
        while carry and i >= 0:
            carry, digits[i] = divmod(digits[i] + 1, 10)
            i -= 1
        return [digits, [1] + digits][carry]



'''s
执行用时：32 ms, 在所有 Python3 提交中击败了63.56% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了34.48% 的用户
通过测试用例：111 / 111
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = int(''.join(map(str, digits))) + 1
        return list(map(int, list(str(x))))
