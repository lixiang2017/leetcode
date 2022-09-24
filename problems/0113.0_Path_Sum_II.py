'''
BFS
T: O(N)
S: O(NlogN)

Runtime: 38 ms, faster than 99.38% of Python3 online submissions for Path Sum II.
Memory Usage: 15.4 MB, less than 89.27% of Python3 online submissions for Path Sum II.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # (cur_node, cur_sum, path_list)
        q = deque([(root, root.val, [root.val])]) if root else []
        ans = []
        while q:
            cur_node, cur_sum, path = q.popleft()
            if cur_sum == targetSum and not cur_node.left and not cur_node.right:
                ans.append(path)
            if cur_node.left:
                q.append((cur_node.left, cur_sum + cur_node.left.val, path + [cur_node.left.val]))
            if cur_node.right:
                q.append((cur_node.right, cur_sum + cur_node.right.val, path + [cur_node.right.val]))
        return ans 

'''
backtracking
T: O(N)
S: O(logN)

Runtime: 83 ms, faster than 37.77% of Python3 online submissions for Path Sum II.
Memory Usage: 15.5 MB, less than 72.84% of Python3 online submissions for Path Sum II.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        # cur_sum not include the-node-value 
        def backtrack(node, cur_sum, path):
            if not node:
                return 
            cur_sum += node.val
            if not node.left and not node.right and cur_sum == targetSum:
                ans.append(path + [node.val])
                
            path.append(node.val)
            backtrack(node.left, cur_sum, path)
            path.pop()
            path.append(node.val)
            backtrack(node.right, cur_sum, path)
            path.pop()
        
        backtrack(root, 0, [])
        return ans 
