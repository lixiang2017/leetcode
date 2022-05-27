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


'''
sort + backtracking

执行用时：48 ms, 在所有 Python3 提交中击败了88.87% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了30.96% 的用户
通过测试用例：170 / 170
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, cur_arr, remain):
            if remain == 0: 
                ans.append(cur_arr)
                return 
            for j in range(i, n):
                if remain >= candidates[j]:
                    backtrack(j, cur_arr + [candidates[j]], remain - candidates[j])
                else:
                    break 

        backtrack(0, [], target)
        return ans



