'''
approach: backtracking with pruning

You are here!
Your runtime beats 10.32 % of python submissions.
You are here!
Your memory usage beats 7.61 % of python submissions.
'''

class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.permutations = []
        self.backtracking([], n)
        # print 'self permutations: ', self.permutations
        return len(self.permutations)
        
       
      
    # with cut
    permutations = []
    def backtracking(self, path, n):
        if len(path) == n:
            self.permutations.append(path)
        
        for i in range(1, n + 1):
            if i in path:
                continue
                
            if 0 == (len(path) + 1) % i or 0 == i % (len(path) + 1):
                self.backtracking(path + [i], n)
        return self.permutations





'''
Your input
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15


1
2
3
8
10
36
41
132
250
700
750
4010
4237
10680
24679
'''