'''
approach: Backtracking / DFS

执行结果：
通过
显示详情
执行用时：40 ms, 在所有 Python 提交中击败了72.26%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了64.05%的用户
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        candidates.sort()
        size = len(candidates)

        def backtracking(candidates, path, begin, size, residue):

            for i in range(begin, size):
                if residue - candidates[i] < 0:
                    break
                if residue - candidates[i] == 0:
                    combinations.append(path + [candidates[i]])
                    break

                backtracking(candidates, path + [candidates[i]], i, size, residue - candidates[i])
        
        backtracking(candidates, [], 0, size, target)

        return combinations
