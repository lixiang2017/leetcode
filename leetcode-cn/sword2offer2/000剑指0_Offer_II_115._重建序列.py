'''
自己翔了好就都没有思路
看了提示， 是拓扑排序。瞬间就懂了，瞬间就知道怎么写了。

执行用时：244 ms, 在所有 Python3 提交中击败了7.20% 的用户
内存消耗：22.7 MB, 在所有 Python3 提交中击败了5.20% 的用户
通过测试用例：83 / 83
'''
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        if nums == [1] and sequences == [[1]]:
            return True
        n = len(nums)
        class Node:
            def __init__(self, num):
                self.num = num 
                self.children = set()

        # num -> Node
        nodes = dict()
        in_degree = Counter()
        found_cnt = 0
        seen_pairs = set()
        for seq in sequences:
            for a, b in pairwise(seq):
                if a not in nodes:
                    nodes[a] = Node(a)
                    found_cnt += 1
                if b not in nodes:
                    nodes[b] = Node(b)
                    found_cnt += 1
                if (a, b) not in seen_pairs:
                    seen_pairs.add((a, b))
                    in_degree[b] += 1
                nodes[a].children.add(b)

        if found_cnt != n:
            return False 
        
        # topological sort 
        q = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
        if len(q) != 1:
            return False 
        topo = []
        while q:
            num = q.popleft()
            topo.append(num)
            for child in nodes[num].children:
                in_degree[child] -= 1
                if 0 == in_degree[child]:
                    q.append(child)
            # next round
            if len(q) > 1:
                return False 

        return nums == topo 


'''
输入：
[4,1,5,2,6,3]
[[5,2,6,3],[4,1,5,2]]
输出：
false
预期结果：
true
原因： 5->2 这个路径重复计算了

通过测试用例：81 / 83
输入：
[1]
[[1]]
输出：
false
预期结果：
true
# edge case: 子序列长度为 1 
'''

