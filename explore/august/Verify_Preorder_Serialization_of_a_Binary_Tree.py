'''
You are here!
Your runtime beats 5.08 % of python3 submissions.
You are here!
Your memory usage beats 44.60 % of python3 submissions.
'''
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stack = []
        for p in preorder:
            stack.append(p)
            while len(stack) > 2 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack[-1] = '#'
        return stack == ['#']


'''
ref:
https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/solution/pai-an-jiao-jue-de-liang-chong-jie-fa-zh-66nt/

    入度：有多少个节点指向它；
    出度：它指向多少个节点。
在树（甚至图）中，所有节点的入度之和等于出度之和。可以根据这个特点判断输入序列是否为有效的！
diff = 出度 - 入度
由于根节点没有父节点，所以其入度为 0，出度为 2。因此 diff 初始化为 1

这个diff可以理解为“挂度”，即当前树上还剩几个位置可挂节点。初始化为1，可以想象成根节点加入之前就有一个虚拟挂点。每新加入一个节点就减去一个挂度，遇到中间非null节点，则新增两个挂度（左边一个，右边一个）。

            // 每加入一个节点 都要先减去一个入度   若该节点是非空节点 还要再加上两个出度
            // 遍历完之前，出度是大于等于入度的    1个出度认为提供一个挂载点  1个入度认为消耗一个挂载点
            // 若小于等于 消耗的挂载点 大于等于 提供的挂载点  不可能再继续遍历挂载剩下的节点了


You are here!
Your runtime beats 5.08 % of python3 submissions.
You are here!
Your memory usage beats 44.60 % of python3 submissions.
'''
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        diff = 1
        for p in preorder:
            diff -= 1
            if diff < 0:
                return False
            if p != '#':
                diff += 2
        return diff == 0
