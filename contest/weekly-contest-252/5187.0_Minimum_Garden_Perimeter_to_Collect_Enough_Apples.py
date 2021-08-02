'''
304 / 304 个通过测试用例
状态：通过
执行用时: 2788 ms
内存消耗: 18.1 MB
提交时间：9 小时前
'''
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        total = [0]
        i = 0
        while total[-1] < neededApples:
            i += 1
            t_next = total[-1] + 12 * i ** 2
            total.append(t_next)
        return i * 8
