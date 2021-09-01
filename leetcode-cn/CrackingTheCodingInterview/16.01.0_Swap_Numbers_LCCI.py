'''
add
可能会溢出

执行用时：32 ms, 在所有 Python3 提交中击败了76.58% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了21.85% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] += numbers[1]
        numbers[1] = numbers[0] - numbers[1]
        numbers[0] -= numbers[1]
        return numbers


'''
XOR

执行用时：36 ms, 在所有 Python3 提交中击败了54.28% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了71.62% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] ^= numbers[1]
        numbers[1] ^= numbers[0]
        numbers[0] ^= numbers[1]
        return numbers


'''
执行用时：32 ms, 在所有 Python3 提交中击败了76.58% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了47.30% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        return [numbers[1], numbers[0]]
