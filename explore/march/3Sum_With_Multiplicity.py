'''
DFS / backtracking

59 / 71 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
[38,83,7,34,18,91,13,78,14,73,81,78,67,35,39,69,57,84,67,30,47,59,1,1,71,5,45,26,0,55,72,88,81,37,43,7,89,30,35,14,33,70,30,87,23,40,58,88,75,44,46,37,0,73,7,28,6,75,39,27,5,17,96,21,27,9,75,89,99,83,19,91,43,62,42,64,88,18,49,89,30,59,19,55,4,44,42,13,10,84,96,61,15,96,24,16,18,55,16,50,70,13,60,78,58,5,28,0,100,41,53,57,88,10,49,62,33,74,54,62,87,0,31,23,45,93,65,57,50,16,97,37,62,72,11,3,80,96,27,70,53,16,21,94,70,28,97,8,11,2,91,91,68,83,61,47,87,12,66,65,85,61,16,36,66,4,90,91,21,2,38,58,61,45,69,93,98,84,63,91,41,62,26,10,11,65,59,22,52,51,67,39,51,15,93,71,96,14,89,26,33,33,82,74,11,59,87,58,64,44,43,58,62,55,37,72,76,11,84,97,83,34,33,53,49,84,0,98,89,47,64,55,91,27,74,90,33,26,73,31,59,54,9,35,76,73,9,53,14,90,6,70,9,11,9,7,60,87,22,61,72,30,38,72,99,71,39,41,4,58,75,49,33,69,32,68,31,70,35,86,6,0,78,2,87,37,42,78,33,87,7,81,96,72,50,92,78,95,98,17]
130
'''


from operator import mul

class Solution(object):
    choices = 0
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        cntr = Counter(arr)
        MODULO = 10 ** 9 + 7
        distinct = list(set(arr))  # TypeError: 'set' object does not support indexing
        N = len(distinct)
        
        
        def dfs(cnts, distinct, N, idx, remainder, path):
            # print 'cntr: ', cntr
            # print cnts, distinct, idx, remainder, path
            if remainder < 0 or len(path) > 3:
                return
            
            if remainder == 0 and len(path) >= 3 and len(set(path)) <= 3:
                if len(set(path)) == 3:
                    # choices += cntr[path[0]] * cntr[path[1]] * cntr[path[2]]
                    self.choices += reduce(mul, map(cntr.__getitem__, path))
                elif len(set(path)) == 2:
                    ps = Counter(path)
                    one = two = 0
                    for element, seen in ps.iteritems():
                        if seen == 2:
                            two = element
                        if seen == 1:
                            one = element
                    self.choices += cntr[one] * cntr[two] * (cntr[two] - 1) / 2
                elif len(set(path)) == 1:
                    n = cntr[path[0]]
                    self.choices +=  n * (n - 1) * (n - 2) / 6
        
                self.choices %= MODULO
                return
            
            # recursion
            for i in range(idx, N):
                if cnts[distinct[i]] > 0:
                    cnts[distinct[i]] -= 1
                    dfs(cnts, distinct, N, i, remainder - distinct[i], path + [distinct[i]])
                    cnts[distinct[i]] += 1  # need

        cnts = copy.deepcopy(cntr)
        dfs(cnts, distinct, N, 0, target, [])
        return self.choices

    
'''
Input:
[0,0,0]
0
Output:
0
Expected:
1
'''
