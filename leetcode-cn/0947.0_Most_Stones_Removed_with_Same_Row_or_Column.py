'''
approach: Union Find
1. same x -> union
2. same y -> union
3. stone position (x, y) -> union x and y
but if x == y, not union x and y. So we need to differ x from y.(add 10005 to y)

执行结果：通过
显示详情
执行用时：92 ms, 在所有 Python 提交中击败了45.31%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了65.94%的用户
'''

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        uf = UnionFind()
        for stone in stones:
            uf.union(stone[0], stone[1] + 10005)

        return len(stones) - uf.count 

class UnionFind(object):
    def __init__(self):
        self.father = dict()
        self.count = 0

    def find(self, x):
        if x not in self.father:
            self.father[x] = x
            self.count += 1
            print 'in find', self.father
            print 'in find', self.count
            return x

        if self.father[x] == x:
            return x

        return self.find(self.father[x])
    
    def union(self, x, y):
        print 'union ', x, y
        print 'a', self.father
        print 'a', self.count   
             
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        else:
            self.father[rootX] = rootY
            self.count -= 1
        
        print 'b', self.father
        print 'b', self.count


if __name__ == '__main__':
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]] 
    Solution().removeStones(stones)




'''
union  0 10005
a {}
a 0
in find {0: 0}
in find 1
in find {0: 0, 10005: 10005}
in find 2
b {0: 10005, 10005: 10005}
b 1
union  0 10006
a {0: 10005, 10005: 10005}
a 1
in find {0: 10005, 10005: 10005, 10006: 10006}
in find 2
b {0: 10005, 10005: 10006, 10006: 10006}
b 1
union  1 10005
a {0: 10005, 10005: 10006, 10006: 10006}
a 1
in find {0: 10005, 1: 1, 10005: 10006, 10006: 10006}
in find 2
b {0: 10005, 1: 10006, 10005: 10006, 10006: 10006}
b 1
union  1 10007
a {0: 10005, 1: 10006, 10005: 10006, 10006: 10006}
a 1
in find {0: 10005, 1: 10006, 10005: 10006, 10006: 10006, 10007: 10007}
in find 2
b {0: 10005, 1: 10006, 10005: 10006, 10006: 10007, 10007: 10007}
b 1
union  2 10006
a {0: 10005, 1: 10006, 10005: 10006, 10006: 10007, 10007: 10007}
a 1
in find {0: 10005, 1: 10006, 2: 2, 10005: 10006, 10006: 10007, 10007: 10007}
in find 2
b {0: 10005, 1: 10006, 2: 10007, 10005: 10006, 10006: 10007, 10007: 10007}
b 1
union  2 10007
a {0: 10005, 1: 10006, 2: 10007, 10005: 10006, 10006: 10007, 10007: 10007}
a 1
'''