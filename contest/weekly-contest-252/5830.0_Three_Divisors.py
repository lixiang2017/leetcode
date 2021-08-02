'''
227 / 227 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 14.9 MB
提交时间：9 小时前

因子个数为3只有质数的平方数
'''
class Solution:
    def isThree(self, n: int) -> bool:
        if n <= 3:
            return False
        
        div_cnt = i = 0
        while i < n:
            i += 1
            if n % i == 0:
                div_cnt += 1
                if div_cnt > 3:
                    return False
        return 3 == div_cnt
