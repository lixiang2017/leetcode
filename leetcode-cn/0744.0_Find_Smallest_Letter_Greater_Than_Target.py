'''
binary search, T: O(logN), S: O(1)

执行用时：28 ms, 在所有 Python3 提交中击败了97.20% 的用户
内存消耗：16.9 MB, 在所有 Python3 提交中击败了51.85% 的用户
通过测试用例：165 / 165
'''
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        idx = bisect.bisect_right(letters, target)
        if idx == n:
            return letters[0]
        else:
            return letters[idx]

'''
binary search, T: O(logN), S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了30.97% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了34.67% 的用户
通过测试用例：165 / 165
'''
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect.bisect_right(letters, target) % len(letters)]

