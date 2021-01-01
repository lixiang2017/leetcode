'''
Wrong Answer

There is a connection between the former and the latter
'''


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        nums = {}
        for i in range(len(equations)):
            if equations[i][0] not in nums and equations[i][1] not in nums:
                nums[equations[i][0]] = values[i]
                nums[equations[i][1]] = 1.0
            elif equations[i][0] in nums:
                nums[equations[i][1]] =  nums[equations[i][0]] * 1.0 / values[i]
            elif equations[i][1] in nums:
                nums[equations[i][0]] =  nums[equations[i][1]] * 1.0 * values[i]
        
        print nums
        res = []
        for query in queries:
            if query[0] in nums and query[1] in nums:
                res.append(nums[query[0]] * 1.0 / nums[query[1]])
            else:
                res.append(-1.00000)
        
        return res


if __name__ == '__main__':
	equations = [["a","b"],["e","f"],["b","e"]]
	values = [3.4,1.4,2.3]
	queries = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
	print Solution().calcEquation(equations, values, queries)
