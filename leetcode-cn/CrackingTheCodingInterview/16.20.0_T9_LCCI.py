'''
Hash Table + Hash Set

执行用时：28 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了14.02% 的用户
通过测试用例：33 / 33
'''
class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        m = {
            '2': {'a', 'b', 'c'},
            '3': {'d', 'e', 'f'}, 
            '4': {'g', 'h', 'i'}, 
            '5': {'j', 'k', 'l'}, 
            '6': {'m', 'n', 'o'}, 
            '7': {'p', 'q', 'r', 's'}, 
            '8': {'t', 'u', 'v'}, 
            '9': {'w', 'x', 'y', 'z'}, 
        }
        ans = []
        for w in words:
            valid = True
            for n, ch in zip(num, w):
                if ch not in m[n]:
                    valid = False
                    break
            if valid:
                ans.append(w)
        return ans



'''
执行用时：76 ms, 在所有 Python3 提交中击败了26.22% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了5.49% 的用户
通过测试用例：33 / 33
'''
class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        # key = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 
        # 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
        key = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5',
         '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '9', '9', '9', '9']
        ans = []
        for w in words:
            dec = ''.join([key[ord(ch) - ord('a')] for ch in w])
            if dec == num:
                ans.append(w)
        return ans
        