'''
You are here!
Your runtime beats 23.13 % of python submissions.
You are here!
Your memory usage beats 28.97 % of python submissions.
'''


class Solution(object):
    def __init__(self):
        self.result_all = None
        self.directs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.m = 0
        self.n = 0
        self.pa = None # can flow to pacific
        self.at = None # can flow to atlantic
        self.visited = None
        
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        self.result_all = []
        self.m, self.n = len(matrix), len(matrix[0]) if matrix else 0
        if self.m == 0:
            return self.result_all
        self.pa = [[0] * self.n for _ in range(self.m)]
        self.at = [[0] * self.n for _ in range(self.m)]
        self.visited = [[0] * self.n for _ in range(self.m)]
        
        # from top
        for i in range(0, 1):
            for j in range(self.n):
                self.dfs(matrix, i, j, True)
        # from left
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(0, 1):
                self.dfs(matrix, i, j, True)
        # from bottom
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m - 1, self.m):
            for j in range(self.n):
                self.dfs(matrix, i, j, False)
        # from right
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n - 1, self.n):
                self.dfs(matrix, i, j, False)
        
        for i in range(self.m):
            for j in range(self.n):
                if self.pa[i][j] and self.at[i][j]:
                    self.result_all.append((i, j))
        return self.result_all
    
    def dfs(self, matrix, i, j, flag):
        if self.visited[i][j]:
            return
        self.visited[i][j] = 1
        if flag: # can flow to pacific
            self.pa[i][j] = 1
        else: # can flow to atlantic
            self.at[i][j] = 1
        
        for k in range(4):
            x = i + self.directs[k][0]
            y = j + self.directs[k][1]
            if not self.in_area(x, y):
                continue
            if matrix[i][j] > matrix[x][y]:
                continue
            self.dfs(matrix, x, y, flag)
        return
    
    def in_area(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n
            