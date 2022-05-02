'''
同时在线获取

执行用时：3928 ms, 在所有 Python3 提交中击败了5.77% 的用户
内存消耗：25.9 MB, 在所有 Python3 提交中击败了5.29% 的用户
通过测试用例：48 / 48
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(node: TreeNode):
            if node:
                yield from inorder(node.left)
                yield node.val 
                yield from inorder(node.right)
        
        it1, it2 = inorder(root1), inorder(root2)
        ans = []
        v1, v2 = next(it1, None), next(it2, None)
        while True:
            if v1 is not None and v2 is not None:
                if v1 < v2:
                    ans.append(v1)
                    v1 = next(it1, None)
                else:
                    ans.append(v2)
                    v2 = next(it2, None)
            # elif (v1 or v2):  # wrong, maybe zero in values, must check None
            elif v1 is None and v2 is not None:
                ans.append(v2)
                v2 = next(it2, None)
            elif v1 is not None and v2 is None:
                ans.append(v1)
                v1 = next(it1, None)
            else: # if v1 is None and v2 is None:
                break

        return ans 


'''
[0,-10,10]
[5,1,7,0,2]

[]
[5,1,7,0,2]
'''


'''
merge

执行用时：3252 ms, 在所有 Python3 提交中击败了5.77% 的用户
内存消耗：23.8 MB, 在所有 Python3 提交中击败了70.67% 的用户
通过测试用例：48 / 48
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(node: TreeNode):
            if node:
                yield from inorder(node.left)
                yield node.val 
                yield from inorder(node.right)
        
        vs1, vs2 = list(inorder(root1)), list(inorder(root2))
        m, n = len(vs1), len(vs2)
        ans = []
        i = j = 0
        while i < m and j < n:
            if vs1[i] < vs2[j]:
                ans.append(vs1[i])
                i += 1
            else:
                ans.append(vs2[j])
                j += 1
                
        ans += vs1[i: ] + vs2[j: ]
        return ans 





