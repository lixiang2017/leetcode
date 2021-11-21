'''
40 / 40 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 15 MB
提交时间：12 小时前
'''
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        left = cap
        steps = 0
        for i, p in enumerate(plants):
            if left >= p:
                left -= p
                steps += 1
            else:
                steps += i
                steps += i + 1
                left = cap - p
         
        return steps
