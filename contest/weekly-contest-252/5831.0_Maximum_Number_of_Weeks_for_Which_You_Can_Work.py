'''
假设A、B、C、D四种任务。（其他种情况均类似）
AAAAAAAA...AAAAAAAAAAAA
BBBBB....BBBBBBB
CCCC...CCCCCCC
DDD...DDD

两种情况。
1、rest < longest, 如何安排呢？
假设A有无穷多个，先消耗B，再消耗C，再消耗D...
ABABABAB...AB    # 消耗完B     (下面接着安排)
ACACAC.....AC    # 再消耗完C
ADAD.......AD    # 再消耗完D
A                # 还可以再做个A
这样，结果是 2 * rest + 1
Q：有没有比以上方法更优（做任务再多的）的方案了呢？
A: 应该没了，顶多也就把里面的B/C/D换换顺序。个数还是这么多。

2、rest > longest,如何安排呢？
假设ABCD个数依次递减。
还是尽量消耗A，然后B、C、D。
ABABABAB...AB    # 消耗完B。这样还可能剩下A
ACACAC.....AC    # 消耗C。两种情况。消耗完A或消耗完C
如果还剩下A，可以按照情况1里继续安排AD 
如果还剩下C，可以这样重新安排开始的AB，中间加上C，即
ABCABCABC...ABAB...ACAC   # 这里的前面的C跟后端的C不会重合，因为A的个数是最多的。
同样的，没有A还有D、E、F...可以这样安排
ABCDABCDABCD....ABCABCABC...ABAB...ACAC      #这是一个整的安排方案
ABCDEABCDE...ABCD....ABCABCABC...ABAB...ACAC     #这是一个整的安排方案
ABCDEFABCDEF...ABCDE...ABCD....ABCABCABC...ABAB...ACAC    #这是一个整的安排方案

这样就可以把所有的任务安排完。根据数据的不同，可能会有多种安排方案。


感想：
1、休息好，有灵感，空间想象力
2、多列举些case,手动模拟感受过程。也别只是空想。


执行用时：60 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：23.6 MB, 在所有 Python3 提交中击败了100.00% 的用户
'''
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        longest = max(milestones)
        total = sum(milestones)
        rest = total - longest
        
        if longest > rest:
            return 2 * rest + 1
        else:
            return total
