'''
backtrack
剪枝/加快搜索的方法：
1、降序，优先使用长的；
2、无效结果提前判断, n < 4 or ms[0] > edge or total % 4
3、加入缓存
4、合理的长度再去回溯，s1 + ms[i] <= edge

执行用时：236 ms, 在所有 Python3 提交中击败了76.62% 的用户
内存消耗：47.4 MB, 在所有 Python3 提交中击败了5.07% 的用户
通过测试用例：185 / 185
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        ms = matchsticks
        ms.sort(reverse=True)
        n, total = len(ms), sum(ms)
        edge = total // 4
        if n < 4 or ms[0] > edge or total % 4:
            return False
        
        @cache
        def backtrack(s1, s2, s3, s4, i):
            if s1 == s2 == s3 == s4 and i == n:
                return True 
            can_make = False 
            if s1 + ms[i] <= edge:
                can_make |= backtrack(s1 + ms[i], s2, s3, s4, i + 1)
            if s2 + ms[i] <= edge:
                can_make |= backtrack(s1, s2 + ms[i], s3, s4, i + 1)
            if s3 + ms[i] <= edge:
                can_make |= backtrack(s1, s2, s3 + ms[i], s4, i + 1)
            if s4 + ms[i] <= edge:
                can_make |= backtrack(s1, s2, s3, s4 + ms[i], i + 1)
            return can_make
        
        return backtrack(ms[0], 0, 0, 0, 1)


'''
s2 != s1
s3 not in (s1, s2)
s4 not in (s1, s2, s3)
之前见到过的就不考虑了

执行用时：76 ms, 在所有 Python3 提交中击败了97.61% 的用户
内存消耗：20.2 MB, 在所有 Python3 提交中击败了6.90% 的用户
通过测试用例：185 / 185
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        ms = matchsticks
        ms.sort(reverse=True)
        n, total = len(ms), sum(ms)
        edge = total // 4
        if n < 4 or ms[0] > edge or total % 4:
            return False
        
        @cache
        def backtrack(s1, s2, s3, s4, i):
            if s1 == s2 == s3 == s4 and i == n:
                return True 
            can_make = False 
            if s1 + ms[i] <= edge:
                can_make |= backtrack(s1 + ms[i], s2, s3, s4, i + 1)
            if s2 + ms[i] <= edge and s2 != s1:
                can_make |= backtrack(s1, s2 + ms[i], s3, s4, i + 1)
            if s3 + ms[i] <= edge and s3 not in (s1, s2):
                can_make |= backtrack(s1, s2, s3 + ms[i], s4, i + 1)
            if s4 + ms[i] <= edge and s4 not in (s1, s2, s3):
                can_make |= backtrack(s1, s2, s3, s4 + ms[i], i + 1)
            return can_make
        
        return backtrack(ms[0], 0, 0, 0, 1)

'''
return self.ans

执行用时：60 ms, 在所有 Python3 提交中击败了98.31% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了29.72% 的用户
通过测试用例：185 / 185
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        ms = matchsticks
        ms.sort(reverse=True)
        n, total = len(ms), sum(ms)
        edge = total // 4
        if n < 4 or ms[0] > edge or total % 4:
            return False
        self.ans = False

        def backtrack(s1, s2, s3, s4, i):
            if self.ans or (s1 == s2 == s3 == s4 and i == n):
                self.ans = True
                return  
            if s1 + ms[i] <= edge:
                backtrack(s1 + ms[i], s2, s3, s4, i + 1)
            if s2 + ms[i] <= edge and s2 != s1:
                backtrack(s1, s2 + ms[i], s3, s4, i + 1)
            if s3 + ms[i] <= edge and s3 not in (s1, s2):
                backtrack(s1, s2, s3 + ms[i], s4, i + 1)
            if s4 + ms[i] <= edge and s4 not in (s1, s2, s3):
                backtrack(s1, s2, s3, s4 + ms[i], i + 1)
        
        backtrack(ms[0], 0, 0, 0, 1)
        return self.ans





