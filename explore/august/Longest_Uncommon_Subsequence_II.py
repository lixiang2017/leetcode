'''
ref: 评论中
https://www.cnblogs.com/grandyang/p/6680548.html
把strs先按数量分成once和more，那么结果一定在once里面
再把once按长度排序之后拿去一个一个和more匹配，匹配的话就break，第一个全都匹配不过的就返回

You are here!
Your runtime beats 26.28 % of python3 submissions.
You are here!
Your memory usage beats 66.03 % of python3 submissions.
'''
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        one, more = set(), set()
        for s in strs:
            if s in one:
                one.remove(s)
                more.add(s)
            elif s not in more:
                one.add(s)
        
        def isSubseq(s, t):
            iterator = iter(t)
            for c in s:
                if c not in iterator:
                    return False
            return True
        
        one = sorted(one, key=len)[:: -1]
        for s in one:
            for t in more:
                if isSubseq(s, t):
                    break
            else:
                return len(s)
        return -1
        