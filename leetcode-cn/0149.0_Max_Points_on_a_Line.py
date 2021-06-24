'''
Hash Table
Time: O(N^2)
Space: O(N^2)

执行用时：64 ms, 在所有 Python3 提交中击败了62.99% 的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了5.14% 的用户
'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
            
        kb2points = defaultdict(set)
        maximum = k = b = 0
        N = len(points)
        for i in range(1, N):
            for j in range(i):
                xi, yi = points[i]
                xj, yj = points[j]
                if xi == xj:
                    k = ('N', xi)
                else:
                    k = (yi - yj) * 1.0 / (xi - xj)
                    b = yi - k * xi

                kb2points[(k, b)].add(tuple(points[i]))
                kb2points[(k, b)].add(tuple(points[j]))
                if len(kb2points[(k, b)]) > maximum:
                    maximum = len(kb2points[(k, b)])

        return maximum


'''
执行结果：
解答错误
显示详情

添加备注
输入：
[[0,0]]
输出：
0
预期结果：
1
'''
