'''
执行用时：44 ms, 在所有 Python3 提交中击败了75.87% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了94.90% 的用户
通过测试用例：68 / 68
'''
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = sorted([(name, height) for name, height in zip(names, heights)], key = lambda p: -p[1])
        return [name for name, height in pairs]

'''
执行用时：36 ms, 在所有 Python3 提交中击败了95.59% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了44.08% 的用户
通过测试用例：68 / 68
'''
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[j] for j in sorted(range(len(names)), key=lambda i: heights[i], reverse=True)]


'''
执行用时：44 ms, 在所有 Python3 提交中击败了75.87% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了51.74% 的用户
通过测试用例：68 / 68
'''
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[j] for j in sorted(range(len(names)), key=lambda i: -heights[i])]


'''
执行用时：32 ms, 在所有 Python3 提交中击败了99.30% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了69.37% 的用户
通过测试用例：68 / 68
'''
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return list(map(names.__getitem__ , sorted(range(len(names)), key=lambda i: -heights[i])))
