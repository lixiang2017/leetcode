'''
UnionFind

坑:
要考虑某些名字不一定在names里，但是在synonyms里.

执行用时：192 ms, 在所有 Python3 提交中击败了86.14% 的用户
内存消耗：19.8 MB, 在所有 Python3 提交中击败了37.95% 的用户
通过测试用例：36 / 36
'''
class UnionFind:
    def __init__(self):
        # name -> freq
        self.names = {}
        self.fa = {}
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx < rooty:
            self.fa[rooty] = rootx
            self.names[rootx] += self.names[rooty]
        elif rootx > rooty:
            self.fa[rootx] = rooty
            self.names[rooty] += self.names[rootx]
    
    def find(self, x):
        if x not in self.fa:
            self.names[x] = 0
            self.fa[x] = x
            return x
        if x == self.fa[x]:
            return x
        return self.find(self.fa[x])

class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        uf = UnionFind()
        all_names = set()
        for n in names:
            name, freq = n.strip(')').split('(')
            uf.names[name] = int(freq)
            uf.fa[name] = name
            all_names.add(name)

        for syn in synonyms:
            syn0, syn1 = syn.strip("()").split(',')
            uf.union(syn0, syn1)
        
        ans = []
        for name in all_names:
            if uf.fa[name] == name:
                ans.append(name + '(' + str(uf.names[name]) + ')')

        return ans


'''
输入：
["a(10)","c(13)"]
["(a,b)","(c,d)","(b,c)"]
输出：
["a(10)","c(13)"]
预期结果：
["a(23)"]
'''

