'''
hash set

执行用时：48 ms, 在所有 Python3 提交中击败了12.89% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了95.56% 的用户
通过测试用例：85 / 85
'''
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        integers = set()
        i, n = 0, len(word)
        while i < n:
            if word[i].isalpha():
                i += 1
            else:
                j = i + 1
                while j < n and word[j].isdigit():
                    j += 1
                integer = word[i: j].lstrip('0')
                integers.add(integer or '0')
                i = j + 1
        return len(integers)

'''
执行用时：20 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了94.22% 的用户
通过测试用例：85 / 85
'''
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(int(each) for each in re.findall(r"[0-9]+", word)))
        