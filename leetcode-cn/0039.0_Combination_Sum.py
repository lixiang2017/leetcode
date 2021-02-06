'''
approach: BackTracking / DFS

执行结果：通过
显示详情
执行用时：504 ms, 在所有 Python 提交中击败了5.27%的用户
内存消耗：14.7 MB, 在所有 Python 提交中击败了5.30%的用户
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []

        def backtracking(path, left):
            if left < 0:
                return 
            if  0 == left:
                # add
                combinations.append(path)
            for cand in candidates:
                backtracking(path + [cand], left - cand)
        
        backtracking([], target)
        combinations = set((tuple(sorted(com)) for com in combinations))
        combinations = [list(com) for com in combinations]
        return combinations
