'''
heap

执行用时：1508 ms, 在所有 Python3 提交中击败了76.92% 的用户
内存消耗：46.1 MB, 在所有 Python3 提交中击败了19.23% 的用户
通过测试用例：87 / 87
'''
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        total_ratio = 0
        h = [(p/t - (p+1)/(t+1), p, t) for p, t in classes]
        heapify(h)
        while extraStudents:
            neg_d, p, t = heappop(h)
            p += 1
            t += 1
            heappush(h, (p/t - (p+1)/(t+1), p, t))
            extraStudents -= 1

        for neg_d, p, t in h:
            total_ratio += p / t 
        return total_ratio / n 
