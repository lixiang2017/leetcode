'''
two pointers
T: O(N)
S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了45.40% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了49.99% 的用户
通过测试用例：21 / 21
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]
            elif s < target:
                i += 1
            else:
                j -= 1
        return []