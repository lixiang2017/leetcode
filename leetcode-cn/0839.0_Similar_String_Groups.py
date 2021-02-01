'''
approach: Union Find

执行结果：
通过
显示详情
执行用时：1328 ms, 在所有 Python 提交中击败了80.00%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了100.00%的用户
'''


class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        size = len(strs)

        uf = UnionFind(size, strs)
        for i in range(size - 1):
            for j in range(i + 1, size):
                if uf.isConnected((strs[i], i), (strs[j], j)):
                    continue
                else:
                    if self.isSimilar(strs[i], strs[j]): # or strs[i] == strs[j]:
                        uf.union((strs[i], i), (strs[j], j))
        
        return uf.componentCount

    def isSimilar(self, word1, word2):
        diff = []
        for letter1, letter2 in zip(word1, word2):
            if letter1 != letter2:
                diff.append([letter1, letter2])
            if len(diff) > 2: return False
        
        if not len(diff):
            return True
        else:
            return diff[0] == diff[1][:: -1]


class UnionFind(object):
    def __init__(self, n, strs):
        self.parent = {(word, idx): (word,idx) for idx, word in enumerate(strs)}
        self.componentCount = n
        self.size = {(word, idx): 1 for idx, word in enumerate(strs)}

    def find(self, x):
        if x == self.parent[x]: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY: return False
        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        self.componentCount -= 1
        return True

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

'''
输入：
["abc","abc"]
输出：
2
预期结果：
1
'''

