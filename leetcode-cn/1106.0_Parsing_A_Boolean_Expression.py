'''
执行用时：100 ms, 在所有 Python3 提交中击败了21.43% 的用户
内存消耗：21 MB, 在所有 Python3 提交中击败了5.36% 的用户
通过测试用例：75 / 75
'''
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def function(s):
            s = s.replace('t', 'True')
            s = s.replace('f', 'False')
            s = s.replace('&', 'andfun')
            s = s.replace('|', 'orfun')
            s = s.replace('!', 'notfun')
            return s 
        
        def andfun(*args):
            ret = True 
            for i in args:
                ret = ret and i 
            return ret 
        
        def orfun(*args):
            ret = False
            for i in args:
                ret = ret or i 
            return ret 
        
        def notfun(a):
            return not a 

        z = function(expression)
        return eval(z)


'''
执行用时：112 ms, 在所有 Python3 提交中击败了10.71% 的用户
内存消耗：21 MB, 在所有 Python3 提交中击败了5.36% 的用户
通过测试用例：75 / 75
'''
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def function(s):
            s = s.replace('t', 'True')
            s = s.replace('f', 'False')
            s = s.replace('&', 'andfun')
            s = s.replace('|', 'orfun')
            s = s.replace('!', 'notfun')
            return s 
        
        def andfun(*args):
            return reduce(and_, args)
        
        def orfun(*args):
            return reduce(or_, args)
        
        def notfun(a):
            return not a 

        z = function(expression)
        return eval(z)


        