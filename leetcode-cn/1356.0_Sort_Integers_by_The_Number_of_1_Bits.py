'''
执行用时：52 ms, 在所有 Python3 提交中击败了42.95% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了95.19% 的用户
通过测试用例：77 / 77
'''
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

'''
执行用时：44 ms, 在所有 Python3 提交中击败了81.09% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了11.01% 的用户
通过测试用例：77 / 77
炫耀一下:
'''
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: (bin(x).count('1'), x))
        return arr 
        
        