'''
dfs + hash table
T: O(N)
S: O(N)

执行用时：56 ms, 在所有 Python3 提交中击败了46.69% 的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了47.32% 的用户
通过测试用例：58 / 58
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        ans = []
        sum_cnt = Counter()
        max_cnt = 0

        def node_sum(node):
            nonlocal max_cnt, ans 
            if not node:
                return 0
            s1 = node_sum(node.left)
            s2 = node_sum(node.right)
            s = s1 + s2 + node.val
            sum_cnt[s] += 1
            if sum_cnt[s] > max_cnt:
                max_cnt = sum_cnt[s]
                ans = [s]
            elif sum_cnt[s] == max_cnt:
                ans.append(s)
            return s 

        node_sum(root)
        return ans 
