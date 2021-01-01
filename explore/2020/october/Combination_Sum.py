'''
You are here!
Your runtime beats 94.87 % of python submissions.
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def dfs(candidates, begin, size, path, result, target): 
            if 0 == target:
                result.append(path)
                return
            
            for index in xrange(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break
                    
                dfs(candidates, index, size, path + [candidates[index]], result, residue)
                
        size = len(candidates)
        if 0 == size:
            return []
        
        result = []
        # sorted(candidates)   # wrong answer, cause not sort in place
        candidates.sort() # candidates = sorted(candidates)   # also ok
        dfs(candidates, 0, size, [], result, target)
        
        return result
        