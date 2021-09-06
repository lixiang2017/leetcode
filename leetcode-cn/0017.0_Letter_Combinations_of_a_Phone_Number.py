'''
Iteration

执行用时：28 ms, 在所有 Python3 提交中击败了89.77% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了80.01% 的用户
通过测试用例：25 / 25
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        digit2letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        N = len(digits)
        for i in range(N):
            if 0 == i:
                ans = list(digit2letter[digits[0]])
            else:
                ans = [ a + ch for a in ans for ch in digit2letter[digits[i]] ]

        return ans


'''
DFS

执行用时：40 ms, 在所有 Python3 提交中击败了27.73% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.05% 的用户
通过测试用例：25 / 25
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        # digit2letter
        d2l = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        N = len(digits)
        
        def backtracking(i, curr):
            if i == N:
                nonlocal ans
                ans = curr
                return 

            d = digits[i]
            if 0 == i:
                curr = list(d2l[d])
            else:
                curr = [pre + ch for pre in curr for ch in d2l[d]]

            backtracking(i + 1, curr)

        backtracking(0, [])
        return ans


'''
Backtracking

执行用时：32 ms, 在所有 Python3 提交中击败了73.34% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了12.42% 的用户
通过测试用例：25 / 25
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        ans = []
        # digit2letter
        d2l = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        N = len(digits)
        
        def backtracking(i):
            if i == N:
                ans.append(''.join(com))
                return
            for ch in d2l[digits[i]]:
                com.append(ch)
                backtracking(i + 1)
                com.pop()

        com = []
        backtracking(0)
        return ans
