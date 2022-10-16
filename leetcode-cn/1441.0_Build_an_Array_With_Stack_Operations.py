'''
simulation

执行用时：36 ms, 在所有 Python3 提交中击败了69.83% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了82.12% 的用户
通过测试用例：49 / 49
'''
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        it = iter(target)
        x = next(it, None)
        for i in range(1, n + 1):
            if x is None:
                break   
            if i != x:
                ans.append('Push')
                ans.append('Pop')
            else:
                ans.append('Push')
                x = next(it, None)
        return ans 


'''
iter + iter

执行用时：36 ms, 在所有 Python3 提交中击败了69.83% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了83.24% 的用户
通过测试用例：49 / 49
'''
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        it = iter(target)
        x = next(it, None)
        stream = iter(range(1, n + 1))
        y = next(stream, None)
        while x is not None and y is not None:
            if x != y:
                ans.append('Push')
                ans.append('Pop')
                y = next(stream, None)   
            else:
                ans.append('Push')
                x = next(it, None)        
                y = next(stream, None)                                        
        return ans 

'''
simplify

执行用时：32 ms, 在所有 Python3 提交中击败了89.39% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了30.73% 的用户
通过测试用例：49 / 49
'''
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        it = iter(target)
        x = next(it, None)
        stream = iter(range(1, n + 1))
        y = next(stream, None)
        while x is not None and y is not None:
            ans.append('Push')
            if x != y:
                ans.append('Pop')  
            else:
                x = next(it, None)        
            y = next(stream, None)
        return ans 
